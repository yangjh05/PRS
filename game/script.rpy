# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('넙죽이', color="#c8ffc8")
image bg kaist = "kaist.png" # images 폴더에 정의
image bg toefl = "toefl.png"
image bg drink = "drink.png"
image nubjuk = "nubjugi.png"
image sajang = "sajang.png"
image friend = "friend.png"
image bg introduce = "introduce.png"
image bg endless = "IMG_8124.HEIC.jpg"
image bg table = "image-3.png"
image bg midterm = "midterm.webp"
image bg major = "major.webp"
image bg inst = "instagram.png"
image bg kamf = "kamf.png"
image bg calll = "call.png"
image bg res = "research.png"
image kwon = "kwon.png"

init python:
    import random
    import math
    course_load = 0
    graduate = 0
    hired = 0
    founder = 0
    home = 0
    attr = 0
    is_engcamp = 1
    renai = 1

    def find_max_category():
        # 4개의 값과 각각의 이름을 튜플로 묶음
        values = [("graduate", graduate), ("hired", hired), ("founder", founder), ("home", home)]
        
        # 최대값을 가진 항목을 찾음
        max_category = max(values, key=lambda x: x[1])
        
        # 최대값의 이름과 그 값을 반환
        return max_category[0], max_category[1]

        # 시그모이드 함수 변형: -3일 때 0에 가깝고 6일 때 1에 가까운 값을 반환
    def sigmoid_transformed(x):
        k = 1  # 기울기를 조정하는 값 (너무 급하지 않게 설정)
        c = 1.5  # 중간값으로 -3과 6의 중간값을 사용
        return 1 / (1 + math.exp(-k * (x - c)))

    # attr 변수를 사용해 선택
    def make_choice(attr):
        probability = sigmoid_transformed(attr)  # attr 값에 따른 확률 계산
        random_value = renpy.random.random()  # 0과 1 사이의 난수 생성

        if random_value < probability:
            return "좋아~"
        else:
            return "싫어"
    
    def make_choice_2(attr):
        probability = 0.7 * sigmoid_transformed(attr)  # attr 값에 따른 확률 계산
        random_value = renpy.random.random()  # 0과 1 사이의 난수 생성

        if random_value < probability:
            return "좋아~"
        else:
            return "싫어"


# 여기에서부터 게임이 시작합니다.
label start:

    # jump finalcredits

    "Choose your language / 언어를 선택하세요"
    menu:
        "English":
            $ renpy.change_language("en")
            $ renpy.restart_interaction()
        "한국어":
            $ renpy.change_language("ko")

    show bg kaist

    "여러분은 기다리고 기다리던 카이스트에 합격했습니다!!"

    "카이스트에 첫발을 들인 당신, 기분이 어떠신가요?"

    menu:
        "대학 생활이 너무 기대되네요!":
            "기대되는 대학생활이 시작됩니다!"
        
        "대학에서 해야할 공부가 걱정되어요..":
            "당신은 대학에서 무엇을 배울지 기대하고 있군요!"

label toefl:    
    show bg toefl

    "하지만 카이스트 입학 전에는 모의토플을 봐야한다는 사실.."

    "모의토플을 준비하시겠습니까?"

    show nubjuk

    menu:
        "열심히 준비해본다":
            $ is_engcamp = 0 if random.random() < 0.7 else 1
            "당신은 모의토플을 열심히 준비했다.."
            $ graduate += 1
            if is_engcamp == 0:
                "당신은 모의토플에 합격해 영캠을 면제받았다!!"
            elif is_engcamp == 1:
                "그럼에도 불구하고 당신은 모의토플에 불합격했다!!"
                "당신은 한달동안 지옥의 영캠을 들어야만 했다.."
        "차라리 그럴 시간에 나가서 논다":
            "영캠을 짼 당신은 모의토플에 불합격했다!!"
            "당신은 한달동안 지옥의 영캠을 들어야만 했다.."
            $ home += 1
            $ founder += 1

    hide nubjuk

label drink_intro:
    show bg drink
    "어찌저찌 학교에 입학하였다!"

    "당신은 새터반 친구들과의 첫 술자리를 가지게 되었다!"

    "그러나 술자리가 아직 어색한지 너무나도 조용했다.."

    "당신은.."

    show nubjuk

    menu:
        "이 상황이 너무나도 답답하다!":
            
            e "아 저 더는 못하겠어요!!!"
            "당신은 술자리에서 뛰쳐나갔다.."
            $ graduate += 1
            jump table
        "술 게임이 하고 싶다.":
            e "넙죽이가 좋아하는 랜덤 게임~"
            "꽤나 갑작스러웠지만 반응은 꽤나 좋은 것 같다."
            $ founder += 1
            $ hired += 1
            $ attr += 1
        "가만히 있는게 좋다고 생각했다.":
            e "..."
            "결국 다른 누군가가 대화를 시작했다.."
            $ home += 1
            $ graduate += 1
    hide nubjuk

label introduce:
    show bg introduce
    transform big_sajang:
        xpos 0.38
        ypos 0.4
        zoom 2

    show sajang at big_sajang
    "사장님" "주문하신 음식 나왔습니다~"
    hide sajang 
    
    "음식에서 모락모락 피어나는 연기는 당신의 대학생활의 설렘을 더욱 커지게 했다!"

    "음식도 나왔으니, 서로 자기소개하는 시간이 시작되었다!"

    "당신은.."

    show nubjuk

    menu:
        "이름을 외치고 병샷을 한다":
            e "안녕하세요! 이 반의 주당을 책임질 김넙죽입니다아아!!!"
            "당신은 소주 한병을 시원하게 들이켰다."
            "새터반의 함성이 술집을 가득 메웠다."
            $ attr += 1
            $ founder += 1
        
        "이름과 학번을 이야기한다":
            e "안녕하세여, 202XXXXX 김넙죽입니다. 잘부탁드립니다."
            "당신은 박수갈채를 받았다."

        "자신에 대한 모든것을 소개시켜준다":
            e "안녕하세요! 저는 김넙죽이고요, 쉬는시간에는.. 평소에는.. 제가 제일 좋아하는것은.. 싫어하는 것은.. 현대사회에서.. 어쩌구 저쩌구.."
            "반응이 별로 좋지 못한것 같다.."
            $ graduate += 1
            $ attr -= 1

    hide nubjuk

label drunk:
    show friend at left
    "친구" "너 MBTI 뭐야?"
    hide friend
    show friend at right
    "친구" "나 뭐같아 보여 ㅋㅋㅋ"
    hide friend
    show friend at left
    "친구" "너 진짜 무조건 E지 ㅋㅋㅋ"
    hide friend

    "어느덧 다들 술에 취한 듯 보인다."
    "당신도 술을 많이 마신듯한 느낌을 받는다.."

    menu:
        "너무 피곤하다. 주체할 수 없는 졸음이 몰려온다.":
            show nubjuk at left
            e "얘들아~ 나 먼저 갈게~"
            hide nubjuk
            show friend at right
            "친구" "뭐야 가는거야?"
            hide friend
            show nubjuk at left
            e "어ㅠㅠ 너무 피곤해애서~ 가볼려고~"
            hide nubjuk

            hide bg

            "..당신은 딱딱한 바닥 위에서 눈을 떴다."
            show bg endless:
                zoom 0.3
            "눈을 떠보니 엔들리스였다!"
            "당신은 술집을 나온 이후에 기억이 없다.."
            "당신은 그대로 엔들리스에서 잠들었던 것이다!"
            $ attr -= 1
            $ founder += 1

        
        "너무 피곤하다. 집에 가고싶은 의지가 강하게 샘솟는다.":
            "당신의 귀소본능은 엄청났다!"
            "기숙사에 도착한 당신은 바로 잠을 청했다.."
            $ hired += 1
        
        "너무 힘들다. 누군가가 도와줬으면 좋겠다.":
            "집에 돌아가는 길 당신은 누군가에게 도움을 요청했다."
            "캠폴" "기숙사가 어디에요 학생?"
            e "저 너무 힘들어요ㅠㅠ 저ㅠㅠ좀 도와주세요ㅜㅜㅜ"
            "캠폴" "알겠으니 학번이랑 기숙사 위치 부르세요. 다음부턴 술 많이 마시지 마세요."
            "당신은 공권력의 도움을 받아 기숙사에 도착했다.."
            $ home += 1
 
label table:
    show bg table

    "새 학기가 시작되기 전에 시간표 신청을 해야 한다... 이번 학기의 시간을 어떻게 구성할지 고민이 된다."

    "하지만 당신에게는 PNR이 있다는 사실!! 당신은 PNR에 대해 궁금하여 친구에게 물어보러 간다."
    show friend
    "친구 1" "PNR? 그거 쓰면 학점만 낮아지는거 아니야..? 안 좋게 보일 수도 있어서 난 다 안쓰려구"
    hide friend
    show friend
    "친구 2" "당연히 써야지!! 나는 그냥 하기싫은거에 3개 박고 이번학기 하고싶은거만 하고 놀거야!"
    hide friend
    show friend
    "친구 3" "난 기계과 갈거라서 편하게 그.. 창시구? 같은데에 PNR쓰고 대충 들으려고~"
    hide friend

    show nubjuk

    menu:
        "기필에 3개를 사용한다":
            "당신은 기본 필수 과목에 PNR을 썼다!."
            $ pnr_choice = "기필"
            $ hired += 1
        
        "악명 높은 OS, 네떡, PL에 PNR을 박는다":
            "당신은 가장 어려운 과목들에 PNR을 박았다...!"
            "당신은 앞으로의 학기가 조금은 걱정된다.."
            $ pnr_choice = "어려운 과목"
            $ founder += 1
            $ home += 1
        
        "훗, 나의 두뇌로 KAIST를 씹어 먹어주지, PNR 버려":
            "당신은 PNR을 버리기로 결정하였다!"
            $ pnr_choice = "PNR 버림"
            $ graduate += 1

    show bg midterm

    "어느덧 첫 중간고사 기간이 다가왔다..."

    if pnr_choice == "기필":
        "당신은 기필에 PNR을 써서 필수 과목들을 안정적으로 마무리할 수 있었다."
        "중간고사 준비가 잘 되어 있어, 자신감이 넘친다!"

    elif pnr_choice == "어려운 과목":
        "어려운 과목에 PNR을 쓴 당신은 그럼에도 불구하고 넘쳐흐르는 과제의 양에 이미 몇개를 드랍한 상태다.."
        "시험을 준비하면서 약간의 불안감이 느껴진다."

    elif pnr_choice == "PNR 버림":
        "당신은 PNR을 사용하지 않고 학업에 도전했다. 고생은 했지만 실력이 많이 늘었다."
        "중간고사가 살짝 긴장된다."

    "갑자기 친구가 나타납니다."

    "친구" "넙죽아~ 술 마시러 갈래?"

    menu:
        "너 공부 안해?":
            "당신은 유혹을 뿌리치고 열심히 공부했다."
            "결국 중간고사에서 좋은 성적을 거두게 되었다."
            $ graduate += 1
        
        "좋아, 마틴 가서 간술하자":
            "당신은 친구와 함께 술을 마시러 갔다."
            "술자리는 즐거웠지만, 공부할 시간이 부족해졌다."
            "당신은 마시고 돌아와서 밤새 시험공부를 해야 했다..."
            $ hired += 1
                    
        "야, 그걸로 되겠어? 태평소까지 달려~~~~~~~~~":
            "당신은 친구와 함께 밤새도록 술을 마셨다."
            "시험은 제대로 망한 것 같다.."
            $ home += 1
            $ founder += 1

    jump cs_selection

label cs_selection:

    show bg major

    "자신의 과를 선택해야 하는 시기가 다가왔다."

    "친구가 나에게 묻는다."

    show friend

    "친구" "넙죽아 너 뭐 신청했는지 보자 ^_^"

    hide friend

    show nubjuk

    menu:
        "당연히 전산이지~ 나는 코딩이 너무 좋아":
            $ graduate += 1
            $ founder += 1
            "당신은 전산학부에 대한 애과심이 넘쳐흘렀다..."
        
        "요새는 전산이 대세지~ 다들 가니까 가려구":
            $ hired += 1
            "당신은 대세를 따라 전산학부에 들어갔다.."
        
        "어 잠시만, 어라 내가 왜 전산이지":
            $ home += 1
            "당신은 어쩌다 전산학부로 흘러들어오게 되었다.."

    jump major_life

label major_life:

    "당신은 전공을 선택한 후 학생회에 가입할 기회를 얻게 되었다."
    "어딘가 야생의 누군가가 달려드는듯한 느낌이 든다.."
    "우왓!!!!"

    # 야생의 학생회가 등장하여 tmi를 늘어놔서 이상한 단체인거 같게 느낌

    show kwon

    "???" "안녕하세요! 저희는 전산학부 집행위원회 <WITH>입니다 🙂"
    "???" "전산학부 집행위원회 하면서 너무 즐거웠어요😎"
    "???" "전산학부 사업 하며 진로와 관련된 정보도 알게 되고📰"
    "???" "LT도 가서 친목도 다지고😉 일하며 경험도 쌓고🧐 학우들에게 도움이 되어 보람찼습니다"
    "???" "진짜 지원 안 하면 후회함!!"
    "???" "슝~"

    hide kwon

    "휴..너무나 갑작스러웠다.."
    "당신은 놀란 마음을 진정시켰다.."
    "학생회에 가입할까?"

    menu:
        "YES":
            "당신은 학생회에 가입하여 다양한 활동을 경험했다."
        
        "YessssssSS!":
            $ attr += 2
            "당신은 학생회의 레전드로 거듭났다..!!!"

    jump relationship

label relationship:
    # show rel

    "그러던 어느 날.."
    "당신은 여느 때처럼 수업에 가는 길이였다.."
    "???" "지코쿠 지코쿠~"
    "저 멀리 뛰어가는 여자아이를 보았다!"
    "그때부터였을까.. 당신은 그 여자아이에게 한눈에 반하고 말았다.."
    "게다가 당신은 그 여자아이가 같은 수업을 듣는다는 사실을 알았다!"

    "납작이를 쳐다본다. 헉! 눈이 마주친다. 당신은.."
    show nubjuk
    menu:
        "생긋 웃는다":
            "당신은 생긋 웃어보였다."
            # 기존의 매력 포인트에 따라 결과가 달라짐
            if attr >= 3:
                $ attr += 2
                "납작이도 생긋 웃어 보였다!"
                "그녀의 웃는 모습에 당신은 두근거렸다.."
            else:
                "납작이의 표정이 굳었다.."
                "당신은 망했다고 생각했다.."
                $ renai = 0
        "피한다":
            "당신은 순간 당황해서 눈을 피했다.."
            if attr >= 3:
                $ attr += 1
                "다시 흘깃 본 당신은 납작이가 웃고 있는 모습을 보았다.."
                "두근거리는 심장에 당신은 수업조차 제대로 들을 수 없었다..!"
            else:
                "납작이는 아무 일 없다는 듯 수업을 듣고 있는듯 하다."
                
        "표정이 굳는다":
            $ attr -= 1;
            "납작이의 표정이 굳었다.."
            "당신은 망했다고 생각했다.."
            $ renai = 0

    "당신은 납작이와 대화하고 싶다고 생각하고 있다.."
    "당신은.."
    menu:
        "\"산책하자\"":
            "당신은 과감히 납작이에게 산책하자고 문자를 보냈다!"
            $ result = make_choice(attr)
            if result == "좋아~":
                "상대방은 기쁘게 산책을 받아들였다."
            else:
                "상대방은 산책을 거절했다."
                $ renai = 0

        "먼저 말을 걸어 주기를 기다린다.":
            $ result = make_choice_2(attr)
            if result == "좋아~":
                "상대방이 먼저 말을 걸어주었다."
            else:
                "아무 일도 일어나지 않았다."
                $ renai = 0
    hide nubjuk
    jump kamf

label kamf:
    show bg kamf

    "KAMF 축제 기간이 다가왔다!!"
    "이번에 초청받은 연예인은.. 넙죽걸스!!"
    "떠오르는 실력파 신예 넙죽걸스가 오지만, 당신은 내일 퀴즈가 있다.."

    show friend
    "친구" "야! 넙죽걸스 보러 갈래?"
    hide friend

    show nubjuk

    menu:
        "공부를 열심히 한다":
            $ graduate += 1
            e "내일이 퀴즈인데 뭔 축제야.."
            "당신은 축제를 포기하고 열심히 공부했다."
        
        "공부 적당히 한다":
            $ founder += 1
            $ hired += 1
            e "나 내일 퀴즈 있어서 공부 좀만 하다가 이따 밤에 갈게!"
            "당신은 낮에 공부하고 밤에는 넙죽걸스를 보러 갔다."

        "공부 안한다":
            $ home += 1
            e "당연하지! 축제 즐기러 가자~~"
            "당신은 축제를 즐기는 것에 집중하기로 했다."
    hide nubjuk
    "당신은 결국 퀴즈를 보러 갔다.."
    $ result = random.choice(["만점", "평균", "0점"])
    if result == "만점":
        $ graduate += 1
        $ hired += 1
        "하지만 당신은 퀴즈에서 만점을 받았다!"
    elif result == "평균":
        $ founder += 1
        "당신은 평균 정도 한것 같다!"
    else:
        $ home += 1
        "당신은 퀴즈에서 0점을 받았다..."
    jump contact

label contact:
    

    if renai != 1:
        jump vacation

    show bg calll

    "축제의 여운이 채 가시지 않았던 그 때, 지난 번 수업에서 내 마음을 잔뜩 흔들어 놓았던 그 사람에게서 연락이 왔다."
    "'까톡🔈'"

    "납작이" "과제 다했어?"

    "미치겠다. 가슴이 너무 두근대고 있다."
    "그렇다고 답장을 안 하고 가만히 있을 수는 없다. 얼른 읽고 대답을 해야 하는데,,,"
    "뭐라고 대답하지?"

    menu:
        "ㅋㅋ 다했지 개쉽던데?":
            $ attr -= 2
            "납작이" "어… 어… 그래? 잘했네,,, 고생했어…!"
            "어라 반응이 왜 이러지? 말을 더 걸어볼까?"
            "..."
            "그 뒤로 납작이와의 연락이 완전히 끊겨 버렸다. 눈물이 나는 건 왜일까?"
            $ renai = 0
        
        "아직 ㅠㅠ 너는?":
            $ attr += 1
            "납작이" "어 나도 하는 중! 혹시 덜 한 거면 우리 같이 만나서 과제할래?"
            "우와! 납작이가 나에게 먼저 만나자고 제안한다! 당연히 가야지!!"
            "그렇게 우리는 커플이 됐다."
        
        "다했는데 좀 어렵더라. 왜 뭐 모르는 거 있어?":
            $ attr += 2
            $ hired += 1
            "납작이" "헐! 너 짱이다 ㅋㅋ"
            "납작이" "나 3번에서.."
            "그렇게 우리는 커플이 됐다."
        
        "아니 과제가 있었어..?":
            $ home += 1
            $ attr -= 1
            "납작이" "그때 교수님이 공지하셨잖아.."
            "..."
            "그 뒤로 납작이와의 연락이 완전히 끊겨 버렸다. 눈물이 나는 건 왜일까?"
            $ renai = 0

    jump vacation

label vacation:

    
    jump research_professor

    

label research_professor:
    show bg res
    "방학이 다가온다. 확신의 J인 넙죽!"
    show nubjuk
    e "이번 방학땐 전산학부 랩실에서 개별연구를 해봐야겠어 …. 어느 랩을 지원하는게 좋을까?"
    hide nubjuk
    "어떤 교수님과 연구를 진행할까?"

    menu:
        "류석영 교수님":
            "So far so good~"
            "'류석영 교수님'의 랩에서 '개별연구'를 완료했다!"
        
        "문은영 교수님":
            "Stay tuned!"
            "'문은영 교수님'의 랩에서 '개별연구'를 완료했다!"

        "권지용 교수님":
            "오늘 밤은 삐딱하게~"
            "'권지용 교수님'의 랩에서 '개별연구'를 완료했다!"

    jump internship

label internship:
    "인턴 지원 기간이 도래했다. 당신이 지원할 회사는?"
    menu:
        "하는 것은 하나도 없고 돈만 받아 간다는 개꿀 회사 대기업 포닉소프트":
            "현재까지의 선택지에 기반하여 분석한다."
            if home > 5:
                "불합격이다.."
                return

            "당신은 합격했다!"
            "당신은 포닉소프트에 합격하여 편하게 인턴십을 마쳤다."
        
        "일이 조금 빡세다고는 하지만 배울 것이 많아 보이는 스타트업 카이프톤":
            "현재까지의 선택지에 기반하여 분석한다."
            if home > 5:
                "불합격이다.."
                return

            "당신은 합격했다!"
            "당신은 카이프톤에 합격하여 많은 것을 배우며 인턴십을 마쳤다."
        
        "이력서를 쓰려 했지만 귀찮아서 포기한다. '이번 방학까지는 그냥 놀자~!'":
            "당신은 이번 방학을 그냥 놀기로 결정했다."
            $ home += 1

    jump finalcredits

label finalcredits:
    scene black
    if find_max_category()[0] == "graduate":
        show screen gradscreen
        pause 100 # 크레딧 스크롤 시간에 맞추어 설정
        hide screen gradscreen
        
        # URL 열기
        $ renpy.run(OpenURL("https://kamf-2024.s3.ap-northeast-2.amazonaws.com/index.html?id=10166354"))
    elif find_max_category()[0] == "hired":
        show screen hiredscreen
        pause 100 # 크레딧 스크롤 시간에 맞추어 설정
        hide screen hiredscreen
        
        # URL 열기
        $ renpy.run(OpenURL("https://kamf-2024.s3.ap-northeast-2.amazonaws.com/index.html?id=609961"))
    elif find_max_category()[0] == "founder":
        show screen founderscreen
        pause 100 # 크레딧 스크롤 시간에 맞추어 설정
        hide screen founderscreen
        
        # URL 열기
        $ renpy.run(OpenURL("https://kamf-2024.s3.ap-northeast-2.amazonaws.com/index.html?id=7721"))
    else:
        show screen homescreen
        pause 100 # 크레딧 스크롤 시간에 맞추어 설정
        hide screen homescreen
        
        # URL 열기
        $ renpy.run(OpenURL("https://kamf-2024.s3.ap-northeast-2.amazonaws.com/index.html?id=62872"))
    
    return

screen gradscreen():
    vbox:
        xsize 1000 # 크레딧의 가로 사이즈
        ysize 2500 # 크레딧의 세로 길이
        xalign 0.5
        yalign 0.0
        at transform:
            subpixel True
            easein 20: # 스크롤 속도 설정
                yalign 1.0
        vbox:
            ysize 720 # 크레딧 시작 전에 빈 화면을 넣기 위해 설정
        text "대학원을 진학한 넙죽이":
            bold True
            size 100
            color "#FFF"
        text "학부 생활의 끝에서, 나는 새로운 도전을 선택했다.":
            xalign 0.5
            color "#FFF"
        text "익숙한 것들을 뒤로하고, 이제는 더 깊은 지식의 세계로 들어간다.":
            xalign 0.5
            color "#FFF"
        text "대학원이라는 이름의 새로운 문이 열리며, 끝없는 연구와 배움의 시간이 나를 기다리고 있다.":
            xalign 0.5
            color "#FFF"
        text "누구도 대신할 수 없는 나만의 길, 그 길을 향한 첫 발걸음이 시작된다. \n이제, 앞으로 나아가 세상에 나의 지식을 새길 차례다.":
            xalign 0.5
            color "#FFF"
        vbox:
            ysize 400 # 여백

screen hiredscreen():
    vbox:
        xsize 1000 # 크레딧의 가로 사이즈
        ysize 2500 # 크레딧의 세로 길이
        xalign 0.5
        yalign 0.0
        at transform:
            subpixel True
            easein 20: # 스크롤 속도 설정
                yalign 1.0
        vbox:
            ysize 720 # 크레딧 시작 전에 빈 화면을 넣기 위해 설정
        text "취직한 넙죽이":
            bold True
            size 100
            color "#FFF"
        text "대학 생활의 끝자락에서, 나는 실전의 무대로 나아가기로 했다.":
            xalign 0.5
            color "#FFF"
        text "학교에서 배운 지식은 이제 현실 속에서 빛을 발할 준비가 되어 있다.":
            xalign 0.5
            color "#FFF"
        text "처음으로 맞이할 사회의 풍경은 낯설고 도전적일지 모르지만, 나의 열정과 노력이 그 모든 장애물을 이겨낼 것이다.":
            xalign 0.5
            color "#FFF"
        text "이제, 나의 능력을 증명할 시간이다. 새로운 환경에서 피어날 나의 성장을 위해.":
            xalign 0.5
            color "#FFF"
        vbox:
            ysize 400

screen founderscreen():
    vbox:
        xsize 1000 # 크레딧의 가로 사이즈
        ysize 3000 # 크레딧의 세로 길이
        xalign 0.5
        yalign 0.0
        at transform:
            subpixel True
            easein 20: # 스크롤 속도 설정
                yalign 1.0
        vbox:
            ysize 720 # 크레딧 시작 전에 빈 화면을 넣기 위해 설정
        text "창업한 넙죽이":
            bold True
            size 100
            color "#FFF"
        text "어렸을 때부터 나는 늘 남들과 조금은 달랐던 것 같다. 누군가는 안정적인 길을 걸어가고 싶어 했지만, 나는 언제나 스스로의 방식으로 문제를 해결해 나가는 것을 좋아했다.":
            xalign 0.5
            color "#FFF"
        text "'이 시험에서의 성적이 내 인생을 결정짓지는 않아. 이런 공부 보다는 현실에 빠르게 적용해 볼 수 있는 나만의 무언가를 만들어 보고 싶어.'":
            xalign 0.5
            color "#FFF"
        text "학생회에 참여하고, 동아리 프로젝트를 이끌면서 팀을 조직하고, 문제를 해결해 나가는 과정 속에서 나는 많은 것을 배웠다. \n특히 그 과정 속에서 '나는 누군가의 지시를 따르는 것보다는, 내 아이디어를 기반으로 세상에 새로운 것을 만들어내는 사람이 되고 싶다'는 확신을 가지게 되었다.":
            xalign 0.5
            color "#FFF"
        text "졸업식이 끝난 지금, 나는 그 어느 때보다도 확신에 차 있다. \n세상이 필요로 하는 새로운 아이디어를 통해 변화를 이끌어가겠다는 결심. 그것이 내가 걸어갈 길이다.":
            xalign 0.5
            color "#FFF"
        text "어쩌면 내가 원했던 것은 항상 이 길이었을지도 모른다. \n안정된 직장, 편안한 생활보다는 내가 만들어갈 무언가를 세상에 보여주고, 그로 인해 사람들에게 영향을 미치고 싶다. \n세상을 바꾸는 작은 움직임은 나로부터 시작될 수 있다. \n이제 나는 그 시작을 위해 첫걸음을 내딛는다.":
            xalign 0.5
            color "#FFF"
        vbox:
            ysize 400

screen homescreen():
    vbox:
        xsize 1000 # 크레딧의 가로 사이즈
        ysize 2500 # 크레딧의 세로 길이
        xalign 0.5
        yalign 0.0
        at transform:
            subpixel True
            easein 20: # 스크롤 속도 설정
                yalign 1.0
        vbox:
            ysize 720 # 크레딧 시작 전에 빈 화면을 넣기 위해 설정
        text "다른 길을 선택한 넙죽이":
            bold True
            size 100
            color "#FFF"
        text "나는 익숙했던 길을 뒤로하고, 전혀 다른 세계로의 도전을 선택했다.":
            color "#FFF"
            xalign 0.5
        text "과학과 공학에서 쌓은 논리와 창의력이 이제는 예술, 법률, 혹은 전혀 다른 분야에서 새롭게 꽃피울 것이다.":
            xalign 0.5
            color "#FFF"
        text "이 길은 나에게 새로운 시야와 경험을 선사할 것이며, 그동안 쌓아온 모든 경험이 이제 또 다른 빛을 발할 준비가 되어 있다.":
            xalign 0.5
            color "#FFF"
        text "낯선 곳에서의 시작, 나의 진정한 열정이 새롭게 피어날 것이다.":
            xalign 0.5
            color "#FFF"
        vbox:
            ysize 400