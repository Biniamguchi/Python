#Brian's solutions

from datetime import datetime
import itertools

class Call(object):

    id = itertools.count().next
    
    def __init__(self, name, phone, reason):
        self.id = "call" + str(Call.id())
        self.time = datetime.now().strftime("%H:%M")
        self.name = name
        self.phone = phone
        self.reason = reason
        self.info = [
            self.id,
            self.time,
            self.name,
            self.phone,
            self.reason
        ]

    def display(self):
        print "---"
        print "ID:", self.id
        print "Time", self.time
        print "Name:", self.name
        print "Phone:", self.phone
        print "Reason:", self.reason
        print "---"


class CallCenter(object):

    def __init__(self):
        self.calls = []
        self.queue = int
    
    def add(self, id):
        self.calls.append(id.info)
        self.queue = len(self.calls)
        return self
    
    def remove(self):
        self.calls.remove(self.calls[0])
        self.queue = len(self.calls)
        return self

    def info(self):
        for call in self.calls:
            print call[2], "-", call[3]
        print "---"
        print "Queue:", self.queue, "calls"
        print "---"


cc = CallCenter()

call0 = Call("Adnan","123-456-7890","Complaint")
cc.add(call0)

call1 = Call("Olu","123-456-7890","Feedback")
cc.add(call1)

call2 = Call("Motuma","123-456-7890","Feedback")
cc.add(call2)

call3 = Call("Andrea","123-456-7890","Appreciation")
cc.add(call3)

call4 = Call("Jon","123-456-7890","Request")
cc.add(call4)

call5 = Call("Eduardo","555-555-5555","Prank")
cc.add(call5)

call0.display()

cc.info()

cc.remove()

cc.info()
# Antony solutions
# calls = []

# class Call(object):
#     def __init__(self,name,phone,time,reason):
#         self.uid    = len(calls)
#         self.name   = name
#         self.phone  = phone
#         self.time   = time
#         self.reason = reason
#         calls.append(self)
#     def display(self):
#         for i in vars(self).items():
#             print i[0]+":",i[1]

# call  = Call("Will","123-123-1231","3:30PM","Prank Call")
# call2 = Call("Dan","987-654-3210","5:30PM","Question about purchase")
# call3 = Call("Minh","456-789-1230","1:30PM","Account assistance")

# class CallCenter(object):
#     def __init__(self):
#         self.calls = []
#         self.queue = len(self.calls)
#     def add(self,call):
#         if type(call) != Call:return
#         self.calls.append(call)
#         self.queue = len(self.calls)
#     def remove(self,phone):
#         call = 0
#         for ind in range(0,len(self.calls)-1):
#             call = self.calls[ind]

#             if call.phone == phone:
#                 print "Removed call from: {}\n".format(call.name)
#                 self.calls.pop(ind)
#                 self.queue = len(self.calls)
        
#     def info(self):
#         for call in self.calls:
#             print call.display(),"queue:{}".format(self.queue),"\n"

# callCenter = CallCenter()
# callCenter.add(call)
# callCenter.add(call2)
# callCenter.add(call3)
# callCenter.info()
# callCenter.remove("987-654-3210")
# callCenter.info()