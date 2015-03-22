#This is a program which allows media professionals to easily create 
#vcf files with contact information of reporters, bloggers, and TV channel contacts. 
#It employs concepts I learned on object oriented programming by using classes and inheritance. 

#This is the original class where we can create media contacts 
class General():
    def __init__(self, first_name, last_name, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.email = email    
            
#This is the class which creates media contacts in the television industry
class TV(General):
    def __init__(self, first_name, last_name, city, email, channel):
        General.__init__(self, first_name, last_name, city, email)
        self.channel = channel
        self.kind = "Television Reporter"

#This is the method to which creates the contact files with the information
    def make_vcard(self):
        vcard= "BEGIN:VCARD\nVERSION:3.0\nFN:%(first_name)s %(last_name)s\nN:%(last_name)s;%(first_name)s;;;\nEMAIL;TYPE=INTERNET;TYPE=WORK:%(email)s\nORG:%(channel)s\nTITLE:%(kind)s\nNOTE:City-%(city)s\nEND:VCARD"
        f = open(self.last_name+self.first_name+".vcf",'w')
        f.write(vcard % {'first_name':self.first_name,
					   'last_name':self.last_name,
					   'email':self.email,
					   'city':self.city,
					   'channel':self.channel,
					   'kind':self.kind})
        f.close()

#This is the class which creates media contacts in the blogger industry
class Blogger(General):
    def __init__(self, first_name, last_name, city, email, website):
        General.__init__(self, first_name, last_name, city, email)
        self.website = website
        self.kind = "Blogger"

#This is the method to which creates the contact files with the information
    def make_vcard(self):
        vcard= "BEGIN:VCARD\nVERSION:3.0\nFN:%(first_name)s %(last_name)s\nN:%(last_name)s;%(first_name)s;;;\nEMAIL;TYPE=INTERNET;TYPE=WORK:%(email)s\nORG:%(website)s\nTITLE:%(kind)s\nNOTE:City-%(city)s\nEND:VCARD"
        f = open(self.last_name+self.first_name+".vcf",'w')
        f.write(vcard % {'first_name':self.first_name,
					   'last_name':self.last_name,
					   'email':self.email,
					   'city':self.city,
					   'website':self.website,
					   'kind':self.kind})
        f.close()


#This is the class which creates media contacts in the print media industry
class Print(General):
    def __init__(self, first_name, last_name, city, email, newspaper):
        General.__init__(self, first_name, last_name, city, email)
        self.newspaper = newspaper
        self.kind = "Print Reporter"
        
#This is the method to which creates the contact files with the information
    def make_vcard(self):
        vcard= "BEGIN:VCARD\nVERSION:3.0\nFN:%(first_name)s %(last_name)s\nN:%(last_name)s;%(first_name)s;;;\nEMAIL;TYPE=INTERNET;TYPE=WORK:%(email)s\nORG:%(newspaper)s\nTITLE:%(kind)s\nNOTE:City-%(city)s\nEND:VCARD"
        f = open(self.last_name+self.first_name+".vcf",'w')
        f.write(vcard % {'first_name':self.first_name,
					   'last_name':self.last_name,
					   'email':self.email,
					   'city':self.city,
					   'newspaper':self.newspaper,
					   'kind':self.kind})
        f.close()


#This below will run our program when this module is run from the command line. We can also import class reporters from a different file to also run the program.
if __name__ == "__main__":
    #These two print statements introduce the program and basic information 
    print "Hello there! This program will help you store media contact information. "
    print "You can also run this module by importing this module into another file and using the methods."
    
    keep_asking = True
    contact_list = []
    while keep_asking:
        kind = raw_input('\n\nWhat type of Reporter do you want to create a file for? Type in "print", "tv", or "blogger" or type "done" if you are finished:  ')
        
        #This part of the program creates files for print media contacts
        if kind == "print":
            first = raw_input('Enter first name:')
            last = raw_input('Enter last name:')
            city = raw_input('Enter city:')
            email = raw_input('Enter their email:')
            newspaper = raw_input('Enter their newspaper:')
            contact_list.append(Print(first, last, city, email, newspaper))
        
        #This part of the program creates files for TV media contacts
        elif kind == "tv":
            first = raw_input('Enter first name:')
            last = raw_input('Enter last name:')
            city = raw_input('Enter city:')
            email = raw_input('Enter their email:')
            channel = raw_input('Enter the tv channel:')
            contact_list.append(TV(first, last, city, email, channel))
                
        #This part of the program creates files for blogger contacts
        elif kind == "blogger":
            first = raw_input('Enter first name:')
            last = raw_input('Enter last name:')
            city = raw_input('Enter city:')
            email = raw_input('Enter their email:')
            website = raw_input('Enter their website:')
            contact_list.append(Blogger(first, last, city, email, website))
        
        #This part of the program helps us complete the program when we are done
        elif kind == 'done':
            break
            
        else:
            print "I do not understand that command"
            
    #This part of the program creates the actual files and then prints out the names of the contacts for which we have created files"
    for instance in contact_list:
        instance.make_vcard()
        print "A file has been created for " + str(instance.first_name)
    
    
    
