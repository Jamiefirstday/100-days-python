print('''

                          __..__             
                      _.sMSMMMMMMb.          
                   .-"TMMMMSMMMMMMMb.    
                 .'    TMMMMSMMMMMMMMb       
                /       TMMMSMMMMMMSSS;      
               :        :MMMMSMMMSSMMMM;     
               ;       @ MMMMSMMSMMMMMMS     
              :    _,   ,P"TMSMSMMMMMMSM     
              : .+""`,  :    `TMMMMMSSMM     
               ) c),     `-,-=,TSSSSMMMM     
              /  `         ,-;|MMMMMMMM;     
             /     _.'(o)  '-';SMSSSSSS      
            (  ,   o       ,-"'`^MMMM'       
             )`            :`.    .'         
             )-.           ;  `- /           
             \         _.-'     :            
             (     _.-"   `.     \           
              "---"--.      \     \          
                      `.     \     \         
                   bug  \       _.sSb        
                         \ _.sSSSSSSSb       
                         dSSSSSSSSP^" \      
                         SSSP^" ___    \     
                        /    .gP""""Tp. \    
                       :    d'     .  `b \   
                       ;   d'       o  `b ;  
                      /   d;            `b|  
                     /,   $;          @  `:  
                    /'    $$               ; 
                  .'      $$b         (o)  | 
                .'       d$$$;             : 
               /       .d$$$$;          ,   ;
              d      .d$$$$$$$          $   |
             :bp.__.g$$$$$$$$$         :$   ;
             $$$$$$$$$$$$$$$$$         $$b : 

''')
print("Welcome to Cyberpunk city 4.7.")
print("Your life is miserable and are barely alive in this cyberpunk world.") 
print("Having had enough, you need to find a way to fight back the evil corporates in this world.")

#game start here
choice1 = input("Which career path do you want to choose? \"Warrior\" or \"Business man\"?").lower()
if choice1 == "warrior":
    #continue the game
    choice2 = input("You successfully became warrior because of your bravery. Do you want to have teammates? \"Y\" or \"N\"?").lower()
    if choice2 == "y":
        #continue the game
        choice3 = input("You got chosen to the biggest team in the city and make lots of friends. But a protest happened after few months. Do you want to be loyal to your team? \"Y\" or \"N\"?").lower()
        if choice3 == "n":
            #continue the game
            choice4 = input("You successfully became the number one warrior. Your skills and power make you the leader of the city. Now, what will be your next step? \"Fight\", \"Retire\" or \"Negotiate\"?").lower()
            if choice4 == "fight":
                print("You saved the poor and punished the rich. However, someone like you is planning to fight back like you did before. That person is now after you for life.")
            elif choice4 == "retire":
                print("You lived a wealthy retire life. But millions of people died and suffered every single day. You are now a lonely and cruel person.")
            else:
                print("You got murdered immediately. The corporates is too powerful and do not keep their promises.")
        else:
            #game over
            print("You got killed by the government. You were framed by the brother you trusted most. Game Over....")
    else:
         #game over
         print("You got killed on your first mission with stupid plan and weak body skills. Game Over....")
else:
    #game over
    print("Because of your lack of intelligence, you failed in the competitive business war. Game Over....")