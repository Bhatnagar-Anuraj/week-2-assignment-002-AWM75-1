import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)

def generate_pattern(): 

    num_rows = 6        # Number of rows in the pattern.
    num_cols = 6        # Number of columns in the pattern.
    spacing = 4.0       # Distance between object centers.

    for row in range(num_rows):
        for col in range(num_cols):
            # Generates the coradinates 
            cube_x = col * spacing 
            cube_z = row * spacing 

            # This divides rows and cols by 3 to see if it equals 0  
            if (row + col) % 3 == 0:
                # Gives a Name to the small cube
                cube_name = f"SmallCube_{row}_{col}"
                # This sets the name and the dimentions fo the Small Cube 
                SmallCube = cmds.polyCube(name=cube_name, w=2, h=4, d=1)[0]
                # This moves the small cube in the air 
                cmds.move(cube_x + 2.5, 8.51, cube_z, SmallCube)
            # This divides rows and cols by 3 to see if it equals 1
            elif (row + col) % 3 == 1:
                # Gives a Name to the Tall cube
                cube_name = f"TallCube_{row}_{col}"
                # This sets the name and the dimentions fo the Tall Cube 
                TallCube = cmds.polyCube(name=cube_name, w=4, h=9, d=2)[0]
                # This moves the Tall cube in the air 
                cmds.move(cube_x - 1.5, 2, cube_z, TallCube)
            # This is what is left if none of them equal 1 or 0     
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

# cd assignment 
test_assignment.py