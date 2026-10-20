
from pyscript import document


club_members = [
    "Kevin Durant",
    "Michael Jordan",
    "LeBron James",
    "Stephen Curry",
    "Kobe Bryant"
]


def check_candidate(event):
    
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()


    full_name = first_name + " " + last_name

  
    is_member = full_name in club_members

   
    messages = {
        True: "Congratulations " + full_name +
              "! You are now part of the ICT club.",
        False: "Sorry " + full_name +
               ", your name is not on the list."
    }

    document.getElementById("result").innerText = (
        messages[is_member]
    )
