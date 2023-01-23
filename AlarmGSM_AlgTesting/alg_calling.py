# Тестирование алгоритма обзвона абонентов.

from enum import Enum

contactList = [
    '+79143701845',
    '+79148989567',
    '+79226887534',
    '+79563689378'
]

diSate = {
    'di-1' : False,
    'di-2' : True,
    'di-3' : False,
    'di-4' : False,
    'di-5' : False,
    'di-6' : True
}

class callMode(Enum):
  GENERAL = 0
  EXLUSIVE = 1
    
def DiCheck(di:dict):
    alCount = 0
    for key, value in di.items():
        print(f"DI: {key}  State: {value} ")
        if(value == True):
            alCount += 1
    return alCount
    
# alStatus = DiCheck(diSate)
    
# if(alStatus > 0):
#     print(f'Alarm enable: {alStatus}')    
# else:
#      print('No alarms')    
     
def CallSubscriber(phone, di:dict):
    answerResult = False
    print('============== CallSubscriber ================')    
    print(f'Call to: {phone}')
    answer = input('Accept call? (y/n)')
    if(answer == 'y'):
        print('Accepted OK')
        print('Alarm DI:')
        DiCheck(di)
        answerResult = True
    else: 
        print('Call declined')
        answerResult = False   
        
    print('============== CallSubscriber End ============')        
    return answerResult

def SendMessageSubcsriber(phone, di:dict):
    print('============ SendMessageSubcsriber ============')    
    print(f'Alarm message to {phone}:') 
    DiCheck(di)   
    print('========= SendMessageSubcsriber End ===========')    

def ClearAlarms(di:dict):
    for key, value in di.items():
        if(value == True):
            di[key] = 'False'
    return di         

     
def AlarmCalling(contact:list, mode:callMode, di:dict):
    copyStatus = di.copy()
    # DiCheck(copyStatus)
    while(DiCheck(copyStatus) > 0): # Крутимся пока есть события

        for callnum in contact: # Перебираем лист с контактами
            
            answStatus = False  # Статус ответа на вызов
            callCounter = 0     # Счетчик попыток дозвона
        
            while((answStatus == False) and (callCounter < 3)): # Выполняем более 3 раз пока не ответил абонент
                callCounter += 1 
                print(f'Call count: {callCounter}')
                answStatus = CallSubscriber(callnum, copyStatus)
            if(answStatus == False):
                SendMessageSubcsriber(callnum, copyStatus)
            elif(answStatus == True):
                if(mode.EXLUSIVE):
                    # for key, value in copyStatus.items():
                    #     if(value == True):
                    #         copyStatus[key] = 'False'    
                    copyStatus = ClearAlarms(copyStatus)   
        if(mode.GENERAL):
            copyStatus = ClearAlarms(copyStatus)                               
            
        
AlarmCalling(contactList, callMode.GENERAL, diSate)        