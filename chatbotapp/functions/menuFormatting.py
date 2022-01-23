

from chatbotapp.kakaojsonformat.response import insert_replies, make_reply


def menuFormat(title, menu):
    text = "\n" + title + "\n"
    Array = menu.split(",");
    for item in Array:
        text += item + '\n'
            
    return text;

def makeWeekendReply(branch, answer):

    reply = make_reply("월", "월요일"+branch)
    answer = insert_replies(answer, reply)

    reply = make_reply("화", "화요일"+branch)
    answer = insert_replies(answer, reply)
        
    reply = make_reply("수", "수요일"+branch)
    answer = insert_replies(answer, reply)
        
    reply = make_reply("목", "목요일"+branch)
    answer = insert_replies(answer, reply)
        
    reply = make_reply("금", "금요일"+branch)
    answer = insert_replies(answer, reply)
    
    reply = make_reply("문의사항", branch+"문의사항")
    answer = insert_replies(answer, reply)
    return answer
