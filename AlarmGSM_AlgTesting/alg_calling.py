# Тестирование алгоритма обзвона абонентов.

from enum import Enum

contactList = [
    '+79143701845',
    '+79148989567',
    '+79226887534',
    '+79563689378'
]


# diSate = {
#     'di-1' : False,
#     'di-2' : True,
#     'di-3' : False,
#     'di-4' : True,
#     'di-5' : False,
#     'di-6' : False
# }

class InputAlarm:
    
  curState = {  
  'di-1' : False,
  'di-2' : False,
  'di-3' : False,
  'di-4' : False,
  'di-5' : False,
  'di-6' : False    
  }
  
  alrmCkeck = {  
  'di-1' : False,
  'di-2' : False,
  'di-3' : False,
  'di-4' : False,
  'di-5' : False,
  'di-6' : False    
  }
  

class callMode(Enum):
  GENERAL = 0
  EXLUSIVE = 1
    
def DiCheck(di:dict):
    alCount = 0
    for key, value in di.items():
        # print(f"DI: {key}  State: {value} ")
        if(value == True):
            alCount += 1
    return alCount

def GetAlarmDi(di:dict):
    alStr = str()
    for key, value in di.items():
        # print(f"DI: {key}  State: {value} ")
        if(value == True):
            alStr += f"\nDI: {key}  State: {value}"
    return alStr
    
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
        print(GetAlarmDi(di))
        answerResult = True
    else: 
        print('Call declined')
        answerResult = False   
        
    print('============== CallSubscriber End ============')        
    return answerResult

def SendMessageSubcsriber(phone, di:dict):
    print('============ SendMessageSubcsriber ============')    
    print(f'Alarm message to {phone}:') 
    print(GetAlarmDi(di))   
    print('========= SendMessageSubcsriber End ===========')    

def ClearAlarms(di:dict):
    for key, value in di.items():
        if(value == True):
            di[key] = 'False'
    return di         

     
def AlarmCalling(contact:list, mode:callMode, di:InputAlarm):
    copyStatus = di.curState.copy()

    while(DiCheck(copyStatus) > 0): # Крутимся пока есть события       

        stopCall = False   

        for i in range(len(contactList)):                                
            answStatus = False  # Статус ответа на вызов
            callCounter = 0     # Счетчик попыток дозвона
        
            while((stopCall == False) and (answStatus == False) and (callCounter < 3)): # Выполняем более 3 раз пока не ответил абонент
                callCounter += 1 
                print(f'Call count: {callCounter}')
                answStatus = CallSubscriber(contactList[i], copyStatus)
            if(answStatus == False):
                SendMessageSubcsriber(contactList[i], copyStatus)
                if(i == (len(contactList) - 1)):
                    copyStatus = ClearAlarms(copyStatus)
                    print('Clear Alarm - > (answStatus == False)')      
                        
            elif(answStatus == True):
                if(mode == callMode.EXLUSIVE):
                    copyStatus = ClearAlarms(copyStatus) 
                    print('Clear Alarm - > (answStatus == True)')     
                    return
                                     
            if(mode == callMode.GENERAL):
                if(i == (len(contactList) - 1)):
                    copyStatus = ClearAlarms(copyStatus)
                    print('Clear Alarm - > (mode == callMode.GENERAL)')
    return di.alrmCkeck                                    
        
# print(f'Contact list nums: {len(contactList)}')                   
DevInput = InputAlarm()

print(f'DevInput:   \n {DevInput.alrmCkeck}\
                       {DevInput.curState}')
        
# AlarmCalling(contactList, callMode.GENERAL, DevInput.curState)       
# AlarmCalling(contactList, callMode.EXLUSIVE, diSate) 

# print('Real alarm state:')
# print(GetAlarmDi(DevInput.curState)) 