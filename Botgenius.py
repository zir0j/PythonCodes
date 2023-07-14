#Discography of Phoebe Bridgers
phoebe_bridgers_albums = ["Punisher", "Strangers in the Alps"]
phoebe_bridgers_year = [2020, 2017]
phoebe_bridgers_disc = dict(zip(phoebe_bridgers_albums, phoebe_bridgers_year))

#Discography of Julien Baker
julien_baker_albums = ["Little Oblivions", "Turn Out the Lights", "Little Oblivions"]
julien_baker_year = [2021, 2017, 2015]
julien_baker_disc = dict(zip(julien_baker_albums, julien_baker_year))

#Discography of Lucy Dacus
lucy_dacus_albums = ["Home Video", "Historians", "No Burden"]
lucy_dacus_year = [2021, 2018, 2016]
lucy_dacus_disc = dict(zip(lucy_dacus_albums,lucy_dacus_year))

#Some fucntions for the engine
def phoebe_bridgers():
    print("According to Wikipedia, Phoebe Bridgers (born August 17, 1994) is an American singer, songwriter, guitarist and record producer.",
    "She was born and raised in Pasadena, California. She was formerly a member of Sloppy Jane before releasing her debut album",
    "'Stranger in the Alps.' She also recently released her sophomore album, 'Punisher' which got her nominated as", "Best New Artist at the 2020 Grammys")
    print("DISCOGRAPHY:", phoebe_bridgers_disc)

def julien_baker():
    print("According to Wikipedia, Julien Rose Baker (born September 29, 1995) is an American singer, songwriter, and multi-instrumentalist. Her music is noted for its moody quality and confessional lyrical style, as well as frank explorations of issues including spirituality, addiction, mental illness, and human nature.", 
    "Born and raised in suburban Memphis, Tennessee, Baker released her debut album Sprained Ankle (2015) while she was a student at Middle Tennessee State University. The album received critical acclaim and appeared on several 2015 year-end lists.", 
    "Baker subsequently signed to Matador Records and released her second studio album Turn Out the Lights in 2017, to further critical success.")
    print("DISCOGRAPHY:", julien_baker_disc)

def lucy_dacus():
    print("Lucy Elizabeth Dacus (born May 2, 1995) is an American singer-songwriter and producer. Originally from Richmond, Virginia, Dacus attracted attention with her debut album No Burden (2016), which led to a deal with Matador Records. Her second album, Historian, was released in 2018 to further critical acclaim.")
    print("DISCOGRAPHY:", lucy_dacus_disc)
    

def initial_start():
    print("What would you like to know?:")
    print("1. What is boygenius")
    print("2. Who are the members of boygenius?")
    print("3. Where to stream their EP?")
    print("4. Disclaimer.")

#Interface and Looping
def loop():
    print("Would you like to go back to the start? [Type yes/no]")
    reply = input()
    if reply == 'yes':
        initial_interface()
    if reply == 'no':
        print("Thank you for using my small directory! Feel free to contact me for errors and stuff.")
        exit()

def initial_interface():
    print("Hi! I made this small directory for you to know just who is boygenius. Seem interested on who they are? Search what you are looking for!")
    initial_start()
    initial_response = print("[Type '1', '2', '3', or '4']:")
    choice = input()

    if choice == '1':
        print("According to Wikipedia, boygenius is an indie rock supergroup formed in 2018 by American musicians Julien Baker, Phoebe Bridgers, and Lucy Dacus.," 
        "Their self-titled debut EP boygenius was written and recorded at Sound City Studios in Los Angeles")
        print("Bridgers has called the formation of the group “kind of an accident,” wherein each of the members were simply fans of each other's work and then became friends.", 
        "Both Dacus and Bridgers had opened for Baker on separate tours in 2016, and they all ran in similar circles as young up-and-coming performers navigating the indie scene.")
        print("Baker had joked to Dacus years before about a “pipe dream” that they could one day all form a band.", "The three decided to book a co-headlining tour in early 2018, and they originally planned to record a single or a cover so that they could perform something together on stage.", 
        "Upon meeting up that summer, however, they found themselves overwhelmed with ideas, and they ended up forming the band, writing, recording, and self-producing the Boygenius EP in four days, with the process involving almost exclusively women.")
        print("They recently reunited with their debut album titled 'the record' and are currently in their own tour!")
        loop()

    if choice == '2':
        print("The members of boygenius are Phoebe Bridgers, Julien Baker, and Lucy Dacus.")
        print("Would you like to learn more about them? [Type yes/no]")
        second_choice = input()

        if second_choice == 'yes':
            print("Who would you like to know?")
            print("1. Phoebe Bridgers")
            print("2. Julien Baker")
            print("3. Lucy Dacus")
            third_choice = input()

            if third_choice in ('1', '2', '3'):
                if third_choice == '1':
                    print(phoebe_bridgers())
                    loop()
                        
                elif third_choice == '2':
                    print(julien_baker())
                    loop()
                        
                elif third_choice == '3':
                    print(lucy_dacus())
                    loop()
              
    if choice == '3':
        print("You may listen to them on:")
        print("1. Spotify: https://sptfy.com/Koz8")
        print("2. Apple Music: https://apple.co/3HwtQqt")
        print("3. YouTube Music: https://bit.ly/3mIPeyS")
        loop()
    
    if choice == '4':
        print("Hi! I'm not much of a programming fiend but I am making my way into the field of Data Science. From what you can tell, I'm just a fan that is still learning.", 
        "Should you find any errs or misinformation in my little directory, feel free to contact me.", "Furthermore, all is used for educational purposes.")
        loop()

    else:
        print("When there's an ERROR, nothing's really there. Try Again")
        loop()

#Starting Page
initial_interface()
