explode
=======
Description:

Some number of bombs sit in a linear chamber, at time 0. At time 1, the bombs explode. Each 
sends one piece of shrapnel to the left and one piece of shrapnel to the right. At each 
successive time iteration, the pieces move at a constant speed on their due courses, passing 
through each other unimpeded, until all have left the chamber.

Given a String describing the initial locations of the bombs, and an Integer describing their
concussive power, this computes the locations of each piece of shrapnel emitted by the bombs
at each time iteration, and terminates once all have left the chamber. 

The method will take as input a String bombs and an Integer force. bombs will have a "B" at 
each position containing a bomb, and a "." at each empty position. At time 1, the B’s disappear, 
sending one "<" piece of sharpnel to the left, and one ">" piece of shrapnel to the right, each 
moving at the constant speed force. If a "<" and ">" ever occupy the same position at the 
same time, they will be collectively represented by a single "X".

The method will return an array of Strings in which each successive element shows the 
occupied locations at each time unit. The first element shows the initial locations of the 
bombs, using "B" and "." characters. The last element shows the empty chamber at the 
first time that it becomes empty.

explode() accepts its input under the following constraints:

• bombs should contain between 1 and 50 characters, inclusive.
• Each character in bombs should be either a "." or a “B”.
• force should be between 1 and 10, inclusive.
