from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

@tool
def get_web_search(query: str, search_period: str = 'w') -> str:
    """
    웹 검색을 수행하는 함수.

    Args:
        query(str): 검색어
        search_period(str): 검색 기간 ("d": 하루, "w": 1주(기본값), "m": 1달, "y": 1년)

    Returns:
        str: 검색 결과
    """
    wrapper = DuckDuckGoSearchAPIWrapper(
        #region='kr-kr',
        time=search_period
    )
    search = DuckDuckGoSearchResults(
        api_wrapper=wrapper,
        results_separator=';\n'
    )

    return search.invoke(query)
    
@tool
def get_current_time(timezone: str, location: str) -> str:
    """
    현재 시각을 반환하는 함수.

    Args:
        timezone(str): IANA 타임존 문자열 (e.g., "Asia/Seoul", "America/New_York")
        location(str): 사람이 읽기 쉬운 지역명 (e.g., "서울", "뉴욕")

    Returns:
        str: "{timezone} ({location}) 현재 시각 YYYY-MM-DD HH:MM:SS" 형식의 문자열
    """
    try:
        tz = ZoneInfo(timezone)
        now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f'{timezone} ({location}) 현재 시각 {now}'

    except ZoneInfoNotFoundError:
        return f'알 수 없는 타임존: {timezone}'
        



tools = [get_web_search, get_current_time]

if __name__ == "__main__":
    time = tools[1].invoke({"timezone":"Asia/seoul","location":"서울"})
    print(time)

    web_searched = tools[0].invoke({"query":"파이썬","search_period":"m"})
    print(web_searched)