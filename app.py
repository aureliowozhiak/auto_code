from auto_code import AutoCode
code_generator = AutoCode()
import os


def update_if_not_equal(x, y):
    if x != y:
        y = x
    return x, y

default_code_lang = "Python"
default_extension = ".py"

print("""
     __       __            __                                                                                
/  |  _  /  |          /  |                                                                               
$$ | / \ $$ |  ______  $$ |  _______   ______   _____  ____    ______                                     
$$ |/$  \$$ | /      \ $$ | /       | /      \ /     \/    \  /      \                                    
$$ /$$$  $$ |/$$$$$$  |$$ |/$$$$$$$/ /$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |                                   
$$ $$/$$ $$ |$$    $$ |$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$    $$ |                                   
$$$$/  $$$$ |$$$$$$$$/ $$ |$$ \_____ $$ \__$$ |$$ | $$ | $$ |$$$$$$$$/                                    
$$$/    $$$ |$$       |$$ |$$       |$$    $$/ $$ | $$ | $$ |$$       |                                   
$$/      $$/  $$$$$$$/ $$/  $$$$$$$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$/                                    
                                                                                                          
                                                                                                          
                                                                                                          
   __                       ______               __                 ______                   __           
  /  |                     /      \             /  |               /      \                 /  |          
 _$$ |_     ______        /$$$$$$  | __    __  _$$ |_     ______  /$$$$$$  |  ______    ____$$ |  ______  
/ $$   |   /      \       $$ |__$$ |/  |  /  |/ $$   |   /      \ $$ |  $$/  /      \  /    $$ | /      \ 
$$$$$$/   /$$$$$$  |      $$    $$ |$$ |  $$ |$$$$$$/   /$$$$$$  |$$ |      /$$$$$$  |/$$$$$$$ |/$$$$$$  |
  $$ | __ $$ |  $$ |      $$$$$$$$ |$$ |  $$ |  $$ | __ $$ |  $$ |$$ |   __ $$ |  $$ |$$ |  $$ |$$    $$ |
  $$ |/  |$$ \__$$ |      $$ |  $$ |$$ \__$$ |  $$ |/  |$$ \__$$ |$$ \__/  |$$ \__$$ |$$ \__$$ |$$$$$$$$/ 
  $$  $$/ $$    $$/       $$ |  $$ |$$    $$/   $$  $$/ $$    $$/ $$    $$/ $$    $$/ $$    $$ |$$       |
   $$$$/   $$$$$$/        $$/   $$/  $$$$$$/     $$$$/   $$$$$$/   $$$$$$/   $$$$$$/   $$$$$$$/  $$$$$$$/ 
                                                                                                         
    """)

exit = False

while(not exit):
    

    print("\n\n--------------------\n\n")

    code_name = input("Enter code name: ")
    main_function = input("Enter the main function to this code: ")
    is_class = input("This code is a class? (Y/n): ")

    if is_class == "n" or is_class == "N":
        is_class = False
    else:
        is_class = True

    code_lang = input(f"What is the code language? ({default_code_lang})")
    extension = input(f"and the code extension? ({default_extension})")

    if code_lang == "":
        code_lang = default_code_lang
        extension = default_extension
    else:
        code_lang, default_code_lang = update_if_not_equal(code_lang, default_code_lang)
        extension, default_extension = update_if_not_equal(extension, default_extension)

    code_generator.create_code(code_name, main_function, is_class, code_lang, extension)