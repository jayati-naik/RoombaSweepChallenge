 #########  Roomba Sweep Challenge ############

 In Roomba Sweep Challenge, task is to tell the Irona's next move.

 ######### Approach to the problem ############

 This is a classic example of Breadth First Search, which can be solved with a bit of modification of the graph we imagine:

 Step 1:
 * Read the input:
    * Bot's initial location.
    * Size of the Grid.
    * A snap of the grid, marking clean, dirty and bot's current position.

  Step 2:
  * Check added to verify:
    * Bot's current location is not invalid.
    * Passed grid size matches the passed grid.

  Step 3:
  * First we check if the passed grid is already clean. If yes, write DONE to the output.txt and EXIT.
  * Second check to see if bot is on a dirty block, write "CLEAN" to the Output.txt and EXIT.
  * If none of the above matches, traverse the grid to find right next move.

  Step 4:
  * To traverse the grid, we have chosen for a a bit modified Breadth Search.
  * We perform search in two direction:
    * Points on Axis x and y. This is pretty straight forward. Check following points => (x,y+1) (x,y-1) (x+1,y) (x-1,y).
    * Points not on the Axis.
  * Search for points not on axis:
    * We mark bot's current location as origin and then traverse in a co-centric way checking all the nodes at a fixed distance:
    So for example:
    1) Check if we find any dirty nodes on the Axis and decide the next move according the location of dirty cell.
    2) If not found, create list of nodes at a euclidean distance of 1 from origin(Bot's current location) and check for dirty cell.
    3) If not found, create list of nodes at a euclidean distance of 2 from origin(Bot's current location) and check for dirty cell.
    4) Continue to iterate, until we find the nearest dirty block.
    5) AS we have already checked the grid for dirty block, we are sure that we have at least on dirty cell present in the grid.

  Step 5:
  * AWS soon as dirty cell is spotted, compare the dirty cell's location with bot's current location to make decision on the direction of bot to Move. If dirty cell is located on:
    * TOP RIGHT or BOTTOM RIGHT. Move RIGHT.
    * TOP LEFT or BOTTOM LEFT. Move LEFT.
    * Above X Axis. Move UP.
    * Below X Axis. Move DOWN.
    * Left of Y Axis. Move LEFT.
    * RIGHT of Y-axis. Move RIGHT.

  Step 6:
  * Write Next Move to output.exe.
  * EXIT
