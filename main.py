def isBeaten (user_input, bot_input) -> bool :
    result = False

    match user_input:
        case "rock" :
            if bot_input == "scissor" :
                result = True
        case "paper" :
            if bot_input == "rock" :
                result = True
        case "scissor" :
            if bot_input == "rock" :
                result = True
    
    return result

rock_vs_paper = isBeaten("rock", "scissor")
print (f"Does rock beats paper? {rock_vs_paper}")