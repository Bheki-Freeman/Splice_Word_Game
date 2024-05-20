''' A simple program to demonstrate the use of different kinds of Python Data structures
    In this program we will use Stacks, Ques, and the Primitive Ones
    --------------------------------------------------------------------------
    We are actually creating a simple program that will have a multiple users using a servic    -e (like an online service): An Online game to be precise
    The user data will be saved using these data structures
    --------------------------------------------------------------------------
    --------------------------------------------------------------------------
    ----    The Game    ----
    1. Computer Prints a List of 3 Lists of letters on the screen 
       [[l, x, a], [b, c, b], [b, z, u]]
    2. The Player is supposed to tell where do we find a match in the lists
    3. Like (in this case) its: 1b -> List index 1 and the match is b
    4. The user is supposed to do this in a very short time (maybe 5ms), if the 
       fail to do the match, the question is wipped and another one shows 
    5. This could go for about 10 games(sessions) while recording a score whene-
       ver there is a good match(hit)
    6. Then the user will be graded. 
    7. We could add some functionality that if the user looses 3 times in a row 
       maybe they loose a life! Meaning that they can't go to the next level
    --------------------------------------------------------------------------
    --------------------------------------------------------------------------
    We need to take user details, since game will evolve into an online one, and 
    users data will have to be tracked accordingly
'''