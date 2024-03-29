import DB.mdbconn as dd


if __name__ == "__main__":
    '''
    ※※※※ 
    참고하기 바랍니다. 
    본 자료는 고영창님의 진짜 만세력을 참고했습니다.  
    고영창님의 진짜 만세력의 절입시간과 한국천문연구원의 절입시간이 차이가 있습니다. 
    어떤 자료가 맞는지는 제가 천문학도가 아니라 알 수 없고, 다만 한국천문연구원의 자료(1800년~2200년)는 
    제가 알 수 없어서 고영창님의 진짜 만세력 데이터를 참고했으므로, 본 데이터를 역서등으로 참고하실 때 유의하시기 바랍니다. 
    ※※※※ 

    처음 공개했던 음력변환 DB에 필요한 부분이 있다고 해서 만세력 정보를 MySQL DB로 제작하였습니다. 
    본 자료는 양력 1900년 1월 1일 부터 2100년 12월 31일까지의 만세력 정보입니다. 

    만세력을 기초로 제작하였기 때문에 음력변환 DB와 달리 입춘을 년간지의 시작으로 계산하며, 절기를 월간지로 계산하였습니다. 

    cd_no  시퀀스 
    cd_sgi  단기년도 
    cd_sy 양력 년도 
    cd_sm 양력 월 
    cd_sd 양력 일 
    cd_ly 음력 년도 
    cd_lm 음력 월 
    cd_ld 음력 일 
    cd_hyganjee 년도를 기준으로 하는 한문 간지(입춘을 기준으로 함) 
    cd_kyganjee 년도를 기준으로 하는 한글 간지(입춘을 기준으로 함) 
    cd_hmganjee 월을 기준으로 하는 한문 간지(절기를 기준으로함)  
    cd_kmganjee 월을 기준으로 하는 한글 간지(절기를 기준으로함)  
    cd_hdganjee 일을 기준으로 하는 한문 간지 
    cd_kdganjee 일을 기준으로 하는 한글 간지 
    cd_hweek 한문 요일(日, 月, 火, 水, 木, 金, 土) 
    cd_kweek 한글 요일(일, 월, 화, 수, 목, 금, 토) 
    cd_stars 28수(角, 亢, 저, 房, 心, 尾, 箕.....) 
    cd_moon_state 월령(삭/망 : 그믐(합삭)- 달이 안보임/보름(보름달) 
    cd_moon_time 삭/망시간(삭이나 망이 될 때 그 시간: 200608092006) 
    cd_leap_month 윤달 정보(평달 0, 윤달 1) 
    cd_month_size 달의 크기(그 달이 음력 29일 소월인 경우 0, 음력 30일까지 있는 대월인 경우 1) 
    cd_hterms 한문 24절기(立春,雨水,驚蟄,春分,淸明.....) 
    cd_kterms 한글 24절기(입춘,우수,경칩,춘분,청명.....) 
    cd_terms_time  절입시간(200608080053 : 양력 2006년 8월 8일 0시 53분) 
    cd_keventday 특정 기념일(한식,초복,중복,말복) 
    cd_ddi 띠 (쥐,소,호랑이,토끼,용,뱀,말,양,원숭이,닭,개,돼지) 
    cd_sol_plan 양력 기념일(신정,삼일절,개천절 등) 
    cd_lun_plan 음력 기념일(설날,단오,칠월칠석 등) 
    holiday  기념일 (국경일과 법정 공휴일: 1, 아니면 0)
    '''
    ddm = dd.SqliteDB('manseryuk.db')
    # 양력 생년월일
    year = 1970
    month = 1
    day = 1
    time = 1
    birthdata = ddm.GetBirth(year, month, day)
    print(birthdata)
    timedata = ddm.GetTime(time)
    print(timedata)