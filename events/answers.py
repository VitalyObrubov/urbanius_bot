
from tgbot.models import User
from tgbot.handlers.keyboard import make_keyboard

EMPTY = {}
CANCEL = {"cancel":"Отмена"}
CANCEL_SKIP = {"cancel":"Отмена","skip":"Пропустить"}
OK = {"ok":"OK"}
YES_NO = {"yes":"Да", "no":"Нет"}
BACK = {"back":"Вернуться в основное меню"} #
BACK_EV_MNU = {"back_ev":"Вернуться в меню мероприятия"} 
BACK_EV_CLNDR = {"back_clndr":"Вернуться к списку мероприятий"} 

EVENTS_MENU = {
                "calendar":"Календарь мероприятий",
                "requested":"Запрошенные мероприятия"
              }

