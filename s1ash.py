import colorama

banner_with_colour = (
    colorama.Fore.GREEN
    + """\
            ____              .__      
      _____/_   |____    _____|  |__   
     /  ___/|   \__  \  /  ___/  |  \  
     \___ \ |   |/ __ \_\___ \|   Y  \ 
    /____  >|___(____  /____  >___|  / 
         \/          \/     \/     \/  """
    + colorama.Fore.RED
    + """  
                        "the script provider" """
    + colorama.Fore.CYAN
    + """
「this is the project title」
        """
    + colorama.Fore.RESET
)
print(banner_with_colour)
