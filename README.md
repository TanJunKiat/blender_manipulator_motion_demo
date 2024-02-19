
# Manipulator Motion Planning in Blender

<img src="/examples/3_arm_demo/Animation/gifmaker_me.gif"/>

# About

This repository is to provide a simple and easy-to-use alterative for people that work with robotic arms to visualise and do basic offline manipulator motion planning.

Surprisingly, the features in Blender are very relatable and translatable to the context of manipulators, like being able to do either linear or point-to-point motion and to control joint speed.

This README will bring you through on how to start motion planning using Blender and some of the basic functions and features that might be useful for your specific application.

# Getting started
1. Install [Blender](https://docs.blender.org/manual/en/latest/getting_started/installing/index.html)
2. Download/clone this repository
```
git clone https://github.com/TanJunKiat/blender_manipulator_motion_demo
```
3. Open the desired robotic arm blender file (e.g. UR10.blend)

# Basic Usage / Features

## Moving via tool tip reference
1. Creating tool tip reference
<img src="/resources/getting_started/1_moving_via_tool_tip/1_insert_reference.png"  width="250"/>
For the tool tip, we will be using either of these 3, a plain axes, an arrow axes, or a single arrow. 

> [!NOTE]
> While the tool tip is not limited to these (you can freely use any object as a tool tip reference), it is important to note that the tool tip reference is a reference object and the actual tool tip will not follow the reference closely, especially in scenarios where there is no solution to the reference.

> [!TIP]
> The initial location of the tool tip reference should be conicide with the initial position of the physical tool tip, while the robotic arm is in its neutral state.

2. Linking tool tip reference to armature
<img src="/resources/getting_started/1_moving_via_tool_tip/2_linking_tool_tip_reference.png" width="250"/>

- Under "Bone constraint properties" of the last bone, there should be a Inverse Kinematics (IK) element. Change the "Target" to the tool tip reference object that you just created

3. Moving tool tip reference
<img src="/resources/getting_started/1_moving_via_tool_tip/3_moving_tool_tip.png" height="250"/>
The tool tip reference position can be changed under the "Object properties". The location and rotation is at the global frame. Another way is to change the "Delta Transformation" instead to do it in the intial position of the tool tip reference.

> [!TIP]
> To add an actual tool onto the robotic arm, you can parent the tool on the last link of the robotic arm. This will ensure that the motion of the robotic arm will move the physical tool. 

## Inserting keyframes

1. Selecting time frame in timeline
<img src="/resources/getting_started/2_inserting_keyframe/1_time_line.png" height="150"/>

Under the "Timeline" panel, drag the time frame pointer to the desired time frame

> [!TIP]
> Remember to change the frame rate under the "Output Properties" to get the desired translation from timeframe to time.

2. Enabling properties to animate
Next to each property, there is a diamond shaped button. Clicking it adds a keyframe of that property to the timeline.

> [!NOTE]
> The way Blender animation works is that any non-animated property that is inbetween two animated of the same property will interpolated. So make sure to animate properties that you want to keep constant

## Changing Inverse Kinematics settings

Under your armature and the "Object Data Properties" tab, the inverse kinematics property can be found. Users can change the following parameters:

| Property | Description | Remark |
| ------------- | ------------- |------------- |
| IK Solver  | What kind of solver to use | So far, the best performance is the [iTaSC solver](https://docs.blender.org/manual/en/latest/animation/armatures/posing/bone_constraints/inverse_kinematics/introduction.html) |
| Mode  | Which mode to run the iTaSC | There is animation and simulation. Simulation is preferred as it estimates the velocity of the motion. |
| Reiteration  | When to trigger a re-iteration / re-planning | "Always" is preferred as it will perform a re-plan after every frame. |
| Precision  | The maximum variation of the end effector between two successive iterations at which a pose is obtained that is stable enough and the solver should stop the iterations.  | Default: 0.005 |
| Iterations  | The upper bound for the number of iterations. | Default: 1000 |
| Auto Step  | A substep is a subdivision on the time between two frames for which the solver evaluates the IK equation and updates the joint position. | Use this option if you want to let the solver set how many substeps should be executed for each frame. Default is True |
| Solver  | Which inverse Jacobian solver that iTaSC will use. | Default: SDLS |
| Feedback  | Coefficient on end effector position error to set corrective joint velocity.  | Default: 1.0 |
| Max Velocity  | ndicative maximum joint velocity in radian per second.  | Default: 100.0 |
| Steps Min  | Proposed minimum substep duration (in second). The auto step algorithm may reduce the substep further based on joint velocity. | Default: 0.01 |
| Max | Maximum substep duration (in second). The auto step algorithm will not allow substep longer than this value. | Default: 0.06 |


# Intermediate Features
## Toggling tool tip behaviour

<img src="/resources/intermediate_features/toggling_tool_tip_behaviour/1_changing_joint_limits.png" width="250"/>

- Under "Bone constraint properties" of the last bone and the Inverse Kinematics (IK) tab, you can animate the following parameters:

| Property | Description | Remark |
| ------------- | ------------- |------------- |
| Position | To enable position tracking | Default: True |
| Weight | Weight of position control | Default: 1.0 |
| Lock | Constrain position of axis tool tip to target | Default: True for all |
| Rotation | To enable rotation tracking | Default: True |
| Weight | Weight of rotation control | Default: 1.0 |
| Lock | Constrain rotation of axis tool tip to target | Default: True for all |

> [!TIP]
> The way to toggle these properties in animation time is similar to the above mentioned method.

## Changing joint limits

<img src="/resources/intermediate_features/changing_joint_limits/1_changing_joint_limits.png" width="250"/>

Under "Bone constraint properties" of the bones, there should be two properties, "Limit Rotation" and "Limit Location". 

The rotation of a joint is by default about the Y-axis (direction from head to tail of a bone). So the rotation should be removed for the X and Z axes (limit to 0 degree for max and min). The joint angle of the joint can be saturated by setting the limit of the Y-axis.

Since all the joints of a manipulator are rotaries, all the axes in the limit rotation constraint should be set to true and zeros.

# Useful Tips
## Clearing animations
<img src="/resources/useful_tips/clearing_animations/1_clear_animation.png" width="250"/>

1. Select the tool tip reference
2. Select Object > Animation > Clear Keyframes

# Robotic arm catalogue

| Robotic arm  | Brand | Status |
| ------------- | ------------- |------------- |
| UR3  | Universal Robots  |  Available :green_circle: |
| UR3e  | Universal Robots  |  In progress  :yellow_circle: |
| UR5  | Universal Robots  |  Available :green_circle: |
| UR5e  | Universal Robots  |  In pipeline  :red_circle: |
| UR10  | Universal Robots  |  Available :green_circle: |
| UR10e  | Universal Robots  |  In pipeline  :red_circle: |
| UR16e  | Universal Robots  |  In pipeline  :red_circle: |
| UR20  | Universal Robots  |  In pipeline  :red_circle: |
| UR30  | Universal Robots  |  Available :green_circle: |
| ------------- | ------------- |------------- |
| IRB120  | ABB  |  Available  :green_circle: |
| IRB1010  | ABB  |  In pipeline  :red_circle: |
| IRB1090  | ABB  |  In pipeline  :red_circle: |
| IRB1100  | ABB  |  In pipeline  :red_circle: |
| IRB1200  | ABB  |  In pipeline  :red_circle: |
| IRB1300  | ABB  |  In pipeline  :red_circle: |
| IRB1500ID  | ABB  |  In pipeline  :red_circle: |
| IRB1600  | ABB  |  In pipeline  :red_circle: |
| ------------- | ------------- |------------- |
| xArm6  | UFactory  |  Available  :green_circle: |
| ------------- | ------------- |------------- |
| VS-68  | DENSO  |  Available :green_circle: |
| ------------- | ------------- |------------- |

# Examples

### Pick and Place
<img src="/universal_robots/ur3/Animation/gifmaker_me.gif" width="200"/>

### Rotating about a point
<img src="/universal_robots/ur5/Animation/gifmaker_me.gif" width="200"/>

### Scanning
<img src="/ufactory/xarm6/Animation/gifmaker_me.gif" width="200"/> <img src="/universal_robots/ur10/Animation/gifmaker_me.gif" width="200"/> <img src="/abb/irb120/Animation/gifmaker_me.gif" width="200"/>

# Add your own custom robotic arm

1. Import mesh under "File > Import"

<img src="/resources/custom_robotic_arm/1_import_mesh.png" width="250"/>


> [!IMPORTANT]
> The mesh needs to be arranged in the neutral state / starting state so the behaviour will be visually accurate after parenting the bones to the mesh.

2. Create and align bones

<img src="/resources/custom_robotic_arm/2_insert_bone.png" width="250"/>

> [!NOTE]
> The bones do not need to be connected.

> [!NOTE]
> For ease of visualisation, the Y-axis of the bone (which is the direction pointing from the head to tail) represents the direction of rotation of the joint.

3. Parenting bones to mesh

<img src="/resources/custom_robotic_arm/3_bone_parenting.png" width="250"/>

- Switch to Pose mode
- Select the mesh from the "Outliner" panel
- Select the bone that you want to parent
- Parent the bone to the mesh using the "Bone" parenting option

> [!TIP]
> Ctrl+P is the shortcut to bring out the parenting dialog

4. Setting up inverse kinematics
- Select the last bone / joint
- Under "Bone Constraint Properties", add a "Inverse Kinematics" property
- Follow the steps in [here](#moving_via_tool_tip_reference) to set up the tool tip reference
- Follow the steps in [here](#changing-inverse-kinematics-settings) to set up the inverse kinematics of the armature


# Useful information
- [Documentation on Blender animations](https://www.blender.org/features/animation/)
- [Documentation on Blender armatures](https://docs.blender.org/manual/en/latest/animation/armatures/index.html)
- [Documentation on Blender Inverse Kinematics](https://docs.blender.org/manual/en/latest/animation/armatures/posing/bone_constraints/inverse_kinematics/introduction.html)

# Contributors
Tan Jun Kiat - Robotics researcher, currently working in Changi General Hospital as a Simulation Robotics Engineer

Email: tanjunkiat@outlook.sg

LinkedIn: https://www.linkedin.com/in/tan-jun-kiat/

