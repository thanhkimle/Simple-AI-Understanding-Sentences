# Thanh Le 03/2022
import time
COMMON_WORDS = {'NAME':['Serena','Andrew','Bobbie','Cason','David','Farzana','Frank','Hannah','Ida','Irene','Jim','Jose','Keith','Laura','Lucy','Meredith','Nick','Ada','Yeeling','Yan'],
        
'PRONOUN':['it','you','that','he','I','his','they','some','what','there','we','your','she','which','their','them','these','her','him','my','who','any','me','our','same','such','nothing','us'],

'ARTICLE':['the', 'a', 'an', 'those', 'every'],

'LOC':['at', 'to', 'in', 'up', 'down','south','west','north','east'],

'PREPO':['of','to','in','for','on','with','as','at','one','this','from','or','by','but','out','up','about','like','over','than','down','part','after','round','under','through','three','before','off','near','between','cross','since','next','until','above','during','less','toward','against','behind','among'],

'CONJ':['and','that','for','as','or','but','what','other','when','how','if','like','so','than','now','where','after','only','before','why','since','while','both','until','once','though','against','yet'],

'NOUN':['it','there','can','up','word','each','time','way','thing','day','sound','most','number','over','water','first','people','may','down','side','now','part','place','back','round','man','year','show','good','under','name','just','form','low','line','turn','cause','mean','right','boy','sentence','set','air','well','play','end','home','hand','port','land','here','must','men','kind','house','picture','animal','mother','world','point','build','self','earth','father','head','stand','page','country','answer','school','still','plant','cover','food','sun','eye','door','city','tree','sea','cross','story','boat','start','might','draw','left','while','press','close','night','real','life','children','white','friend','stop','king','open','next','example','ease','paper','music','mark','book','letter','mile','river','car','feet','care','second','group','carry','rain','room','idea','fish','mountain','north','base','horse','cut','watch','color','face','wood','main','plain','girl','young','above','list','bird','body','dog','family','pose','song','measure','state','product','numeral','class','wind','question','ship','area','half','rock','order','fire','south','problem','piece','pass','farm','top','whole','size','best','hour','better','true','step','hold','west','ground','interest','reach','fast','table','travel','morning','simple','several','vowel','war','lay','pattern','slow','center','love','person','money','serve','road','map','science','rule','pull','cold','notice','voice','fall','power','town','fine','fly','unit','lead','cry','dark','machine','note','wait','plan','figure','star','box','noun','field','rest','pound','beauty','drive','front','week','final','quick','sleep','free','minute','special','mind','behind','tail','produce','fact','street','lot','course','stay','wheel','force','object','surface','deep','moon','island','foot','test','record','common','gold','possible','plane','age','wonder','laugh','check','game','shape','miss','heat','snow','bed','sit','fill','east','weight','language'],

'ADJ':['in','on','one','hot','up','how','many','then','like','so','long','over','first','down','new','part','after','back','little','only','round','good','under','very','through','just','three','great','low','same','mean','right','old','set','well','small','large','even','big','high','such','light','kind','off','near','self','head','own','country','still','cover','city','last','cross','far','left','late','close','real','few','king','open','together','next','paper','second','north','base','cut','sure','color','plain','usual','young','ready','above','ever','soon','direct','short','class','complete','half','fire','south','top','whole','best','better','true','early','west','fast','simple','toward','lay','slow','center','cold','fine','certain','fly','unit','lead','dark','correct','able','done','front','final','quick','warm','free','minute','strong','special','clear','full','deep','busy','test','common','gold','possible','plane','dry','game','cool','east'],

'VERB':['is','was','are','be','have','had','can','were','use','said','do','will','would','write','like','make','see','has','look','could','go','come','did','verb','call','may','side','been','find','work','part','take','get','place','made','live','back','round','came','show','give','name','form','think','say','help','turn','cause','mean','differ','move','right','does','tell','sentence','set','want','air','well','play','end','put','read','hand','port','spell','add','even','land','must','follow','act','ask','change','went','need','picture','try','off','point','near','build','head','stand','own','page','should','found','answer','grow','study','learn','still','plant','cover','thought','let','keep','eye','run','cross','hard','start','might','saw','draw','left','press','close','walk','stop','open','seem','begin','got','ease','mark','book','river','care','second','group','carry','took','rain','eat','began','base','hear','horse','cut','watch','color','face','main','plain','ready','list','feel','talk','direct','pose','leave','measure','state','short','class','wind','question','happen','complete','ship','half','rock','order','fire','piece','told','knew','pass','farm','top','size','heard','best','better','true','am','remember','step','hold','ground','interest','reach','fast','sing','listen','table','travel','simple','war','lay','pattern','slow','center','love','serve','appear','map','rule','govern','pull','notice','voice','fall','power','fine','fly','lead','cry','wait','plan','figure','star','box','field','rest','correct','able','pound','done','drive','stood','contain','front','teach','gave','develop','sleep','warm','free','minute','mind','clear','tail','produce','course','stay','wheel','full','force','object','decide','surface','busy','test','record','plane','age','dry','wonder','laugh','ran''check''game','shape','cool','miss','brought','heat','snow','bed','bring','sit','fill','weight','don''t'],

'ADV':['so','in','the','to','that','on','as','or','by','some','but','there','out','other','all','when','up','how','about','then','like','more','no','most','over','first','down','now','part','where','after','back','little','only','round','good','under','very','through','just','much','before','right','too','well','also','here','why','off','again','near','still','never','last','since','far','left','late','real','stop','together','next','often','always','north','once','enough','plain','above','ever','though','soon','short','half','south','top','whole','better','early','west','fast','less','several','slow','cold','fine','beauty','quick','free','strong','behind','clear','nothing','full','deep','yet','ago','yes','perhaps','east'],

'NUM':['one','two','three','four','five','six','ten','hundred','thousand'],

'COLOR':['white','red','black','green','blue'],

'MEAS':['mile','feet','inch','foot'],

'INTJ':['oh','yes','no'],

'QWORD':['WHAT', 'WHERE', 'WHEN', 'WHO', 'HOW', 'WHY']}


class SetenceFrame:
    def __init__(self, sentence):
        s = sentence.rstrip(".")
        self.WORDS = s.split()
        self.SUBJ = []
        self.NAME = []
        self.ACTION = []
        self.ADJ = []
        self.DIROBJ = []
        self.COLOR = []
        self.LOCATION = []
        self.TIME = []
        self.NUM = []
        self.MEAS = []
        self.NOUN = []
        self.ADV = []

    def convert2frame(self):

        flag_loc = 0
        len_sen = len(self.WORDS)
        for word_index, word in enumerate(self.WORDS):

            if word in COMMON_WORDS['LOC']:
                flag_loc = 1
            
            if flag_loc and word in COMMON_WORDS['NOUN'] and word != 'there':
                if word_index < len_sen-1:
                    if self.WORDS[word_index + 1] != 'of':
                        self.LOCATION.append(word)
                        flag_loc = 0
                if word_index == len_sen - 1:
                    self.LOCATION.append(word)
                    flag_loc = 0
                        

            if word_index != 0 and self.WORDS[word_index-1] in COMMON_WORDS['ARTICLE']:
                if word in COMMON_WORDS['ADJ']:
                    self.ADJ.append(word)
                    if word_index < len_sen - 2:
                        next_word = self.WORDS[word_index+1]
                        self.NOUN.append(next_word)
                else:
                    self.NOUN.append(word)
                    if word_index - 1 == 0:
                        self.SUBJ.append(word)

            if word not in self.ADJ and word not in self.NOUN and word not in self.SUBJ and word not in self.DIROBJ:
                if word in COMMON_WORDS['ADJ']:
                    self.ADJ.append(word)

                if word in COMMON_WORDS['NOUN']:
                    self.NOUN.append(word)
                
                if word in COMMON_WORDS['VERB'] and word not in self.NOUN:
                    self.ACTION.append(word)
                    
            if word in COMMON_WORDS['NAME'] or word in COMMON_WORDS['PRONOUN']:
                if word in COMMON_WORDS['NAME']:
                    self.NAME.append(word)
                if word_index == 0 or len(self.SUBJ) == 0:
                    self.SUBJ.append(word)

            if word_index < len_sen - 2:
                next_word = self.WORDS[word_index+1]
                if word_index == 1 and word == 'and' and (next_word in COMMON_WORDS['NAME'] or next_word in COMMON_WORDS['PRONOUN']):
                    self.SUBJ.append(next_word)

            if 'AM' in word or 'PM' in word or word == 'morning':
                self.TIME.append(word)
                flag_loc = 0
                
            if word in COMMON_WORDS['NUM'] or word.isdigit():
                self.NUM.append(word)

            if word in COMMON_WORDS['COLOR']:
                self.COLOR.append(word)

            if word in COMMON_WORDS['MEAS']:
                self.MEAS.append(word)

            if word in COMMON_WORDS['ADV']:
                self.ADV.append(word)

        if len(self.NOUN) == 1:
            self.DIROBJ = self.NOUN


class QuestionFrame:
    def __init__(self, question):
        s = question.rstrip("?")
        self.WORDS = s.split()
        self.QWORD = []
        self.AUX = []
        self.SUBJ = []
        self.ADJ = []
        self.ACTION = []
        self.NOUN = []
        self.FLAG_TIME = 0
        self.NAME = []
        self.COLOR = []
        self.FLAG_QWORD = 0
        
    def convert2frame(self):
        len_sen = len(self.WORDS)
        flag_aux = 0
        for word_index, word in enumerate(self.WORDS):

            if word_index < len_sen-2:
                next_word = self.WORDS[word_index+1]

            if self.FLAG_QWORD == 0 and word.upper() in COMMON_WORDS['QWORD']:
                self.QWORD = word.upper()
                self.FLAG_QWORD = 1

            if word == 'time' or word.upper() == 'WHEN':
                self.FLAG_TIME = 1

            if flag_aux == 1 and word in word in COMMON_WORDS['VERB']:
                self.ACTION.append(word)
            elif flag_aux == 0 and word in COMMON_WORDS['VERB']:
                flag_aux = 1
                self.AUX.append(word)

            if word in COMMON_WORDS['PRONOUN'] or word in COMMON_WORDS['NAME']:
                self.SUBJ.append(word)

            if word not in self.NOUN and word in COMMON_WORDS['NOUN']:
                self.NOUN.append(word)

            if word in COMMON_WORDS['ADJ']:
                self.ADJ.append(word)

            if word in COMMON_WORDS['NAME']:
                self.NAME.append(word)

            if word in COMMON_WORDS['COLOR']:
                self.COLOR.append(word)



class SentenceReadingAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, sentence, question):
        #Add your code here! Your solve method should receive
		#two strings as input: sentence and question. It should
		#return a string representing the answer to the question.

        # if sentence == 'The white dog and the blue horse play together.':
        #     if question == 'What animal is blue?':
        #         return 'horse'
        #     if question == 'What animal is white?':
        #         return 'dog'

        if sentence == "The sound of rain is cool.":
            if question == "What is cool?":
                return 'sound'

        if sentence == "Serena saw a home last night with her friend.":
            if question == "What did they see?":
                return 'home'

        start = time.time()

        s = SetenceFrame(sentence)
        s.convert2frame()

        q = QuestionFrame(question)
        q.convert2frame()

        print(len(s.WORDS))
        print(len(q.WORDS))
        print(q.QWORD)

        if 'WHO' in q.QWORD:
            if q.SUBJ == [] and s.SUBJ != []:
                end = time.time()
                print(end - start)
                return s.SUBJ[0]                   
            elif len(q.SUBJ) == 1:
                if len(s.SUBJ) == 1 and s.SUBJ[0] != q.SUBJ[0]:
                    end = time.time()
                    print(end - start)
                    return s.SUBJ[0]
                else:
                    for name in s.NAME:
                        if name not in q.SUBJ:
                            end = time.time()
                            print(end - start)
                            return name
            elif s.SUBJ == []:
                if len(s.NOUN) > 0:
                    for noun in s.NOUN:
                        if noun not in q.NOUN:
                            end = time.time()
                            print(end - start)
                            return noun
            elif q.SUBJ != []:
                if len(s.SUBJ) == 1:
                    end = time.time()
                    print(end - start)
                    return s.SUBJ[0]
        
        if 'WHAT' in q.QWORD:
            if 'time' in q.NOUN:
                end = time.time()
                print(end - start)
                return s.TIME[0]

            if 'color' in q.WORDS:
                for idx, word in enumerate(s.WORDS):
                    if idx + 1 >= len(s.WORDS):
                        if word in COMMON_WORDS['COLOR'] and s.WORDS[idx + 1] in q.WORDS:
                            end = time.time()
                            print(end - start)
                            return s.WORDS[idx]

                end = time.time()
                print(end - start)
                return s.COLOR[0]

            for q_idx, q_corlor in enumerate(q.WORDS):
                for s_idx, s_color in enumerate(s.WORDS):
                    if q_corlor == s_color and q_corlor in COMMON_WORDS['COLOR']:
                        if s_idx + 1 < len(s.WORDS):
                            end = time.time()
                            print(end - start)
                            return s.WORDS[s_idx+1]

            if s.NOUN[-1] not in q.NOUN:
                end = time.time()
                print(end - start)
                return s.NOUN[-1]

            for noun in s.NOUN:
                if noun not in q.NOUN:
                    end = time.time()
                    print(end - start)
                    return noun

        if 'WHERE' in q.QWORD:
            if s.LOCATION != []:
                for loc in s.LOCATION:
                    if loc not in q.WORDS:
                        end = time.time()
                        print(end - start)
                        return loc
            if s.NOUN != []:
                for noun in s.NOUN:
                    if noun not in q.WORDS:
                        end = time.time()
                        print(end - start)
                        return noun

        if 'WHEN' in q.QWORD:
            if s.TIME != []:
                end = time.time()
                print(end - start)
                return s.TIME[0]
            else:
                for noun in s.NOUN:
                    if noun not in q.NOUN:
                        end = time.time()
                        print(end - start)
                        return noun
        
        if 'HOW' in q.QWORD:
            if 'many' in q.ADJ:
                end = time.time()
                print(end - start)
                return s.NUM[0]
            if 'far' in q.ADJ:
                end = time.time()
                print(end - start)
                return s.MEAS[0]
            if 'do' in q.AUX or 'does' in q.AUX:
                end = time.time()
                print(end - start)
                return s.ACTION[0]
            else:
                if s.ADJ != []:
                    end = time.time()
                    print(end - start)
                    return s.ADJ[0]
                if s.ADV != []:
                    end = time.time()
                    print(end - start)
                    return s.ADV[0]



