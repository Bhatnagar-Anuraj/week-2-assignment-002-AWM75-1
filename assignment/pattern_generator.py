"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================

OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.

REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.

GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.

TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.

COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""

import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)


def generate_pattern(): 
    num_rows = 6        # Number of rows in the pattern.
    num_cols = 6        # Number of columns in the pattern.
    spacing = 4.0       # Distance between object centers.
    
    # The range thats set will make it so the loop ends onces it reaches the last number in the rows and cols. 
    for row in range(num_rows):
        for col in range(num_cols):
            # Generates the coradinates 
            cube_x = col * spacing 
            cube_z = row * spacing 
            
            # This divides rows and cols by 3 to get either 1, 2, or 3 
            if (row + col) % 3 == 0:
                # Gives a Name to the small cube
                cube_name = f"SmallCube_{row}_{col}"
                # This sets the name and the dimentions fo the Small Cube 
                SmallCube = cmds.polyCube(name=cube_name, w=2, h=4, d=1)[0]
                # This moves the small cube in the air 
                cmds.move(cube_x + 2.5, 8.51, cube_z, SmallCube)
            
            elif (row + col) % 3 == 1:
                # Gives a Name to the Tall cube
                cube_name = f"TallCube_{row}_{col}"
                # This sets the name and the dimentions fo the Tall Cube 
                TallCube = cmds.polyCube(name=cube_name, w=4, h=9, d=2)[0]
                # This moves the Tall cube in the air 
                cmds.move(cube_x - 1.5, 2, cube_z, TallCube)
                
            else:
                # Gives a Name to the Big cube
                cube_name = f"BigCube_{row}_{col}"
                # This sets the name and the dimentions fo the Big Cube 
                BigCube = cmds.polyCube(name=cube_name, w=4, h=5, d=3)[0]
                # This has the big cube sit on the floor. 
                cmds.move(cube_x, 0, cube_z, BigCube)
               
                # This assigens a color materal 
                material = cmds.shadingNode('lambert', asShader=True)
                # this creates a black materal 
                cmds.setAttr(material + ".color", 0.3,0.3,0.3, type="double3") 

                #This selects the Big Cube and applies the materal 
                cmds.select(BigCube)
                cmds.hyperShade(assign=material)

generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")

python test_assignment.py 