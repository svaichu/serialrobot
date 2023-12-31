

header = """<?xml version="1.0"?>
<robot name="{name}">"""
materials = """
    <material name="yellow">
        <color rgba="1 0.83 0 1"/>
    </material>
    
    <material name="blue">
        <color rgba="0.18 0.16 0.31 1"/>
    </material>
    
    <material name="pink">
        <color rgba="0.85 0.01 0.41 1"/>
    </material>
    
    <material name="purple">
        <color rgba="0.51 0.01 0.39 1"/>
    </material>
"""
footer = """
</robot>"""
template_link = """
    <link name="{name}">
        <visual>
            <geometry>
                <box size="0.4 0.4 {length}"/>
            </geometry>
            <origin rpy="{roll} {pitch} {yaw}" xyz="{x} {y} {z}"/>
        </visual>
    </link>
"""
template_joint ="""
    <joint name="{jname}" type="{jtype}">
        <parent link="{parent.name}"/>
        <child link="{name}"/>
        <origin rpy="0 0 0" xyz="{jx} {jy} {jz}"/>
        <axis xyz="{ax} {ay} {az}"/>
        <limit effort="1000.0" lower="-3.14" upper="3.14" velocity="0.5"/>
    </joint>
""" 

def urdf_write(robot, urdf_path):
    a = " "
    b = " "
    all_links = a.join([template_link.format(**vars(link)) for link in robot.links if link.isLast is not True])
    all_joints = b.join([ " " if link.isBase is True else " " if link.isLast is True else template_joint.format(**vars(link)) for link in robot.links if link.isBase is not True])
    with open(urdf_path, "w+") as f:
        f.write(header.format(**vars(robot)))
        f.write(all_links)
        f.write(all_joints)
        # f.write(materials)
        f.write(footer)
