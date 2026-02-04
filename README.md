# Parameter identification through Physics-Informed Neural Networks

## Overview
This project implements Physics-Informed Neural Networks (PINNs) to predict ship maneuvering motion by integrating physical laws with deep learning. The model leverages the Nomoto ship maneuvering equation to ensure physically consistent motion prediction.

## Problem Statement
Accurate ship maneuvering prediction is essential for maritime safety, navigation control, and autonomous vessel systems. Purely data-driven models may violate physical constraints, leading to unrealistic trajectories. This project addresses this limitation by embedding governing physics into the learning process.

## Mathematical Modeling
- Utilizes the first-order Nomoto maneuvering model
- Represents ship yaw rate dynamics as a differential equation
- Physics constraints are incorporated directly into the loss function

## Methodology
- Formulated ship maneuvering dynamics using the Nomoto equation
- Designed a Physics-Informed Neural Network architecture
- Integrated data loss and physics-based residual loss
- Simulated vessel behavior under varying rudder angles
- Evaluated model performance against physical consistency

## Results
- Achieved stable and physically consistent ship motion predictions
- Improved generalization under unseen maneuvering conditions
- Demonstrated effectiveness of PINNs over traditional neural networks
  
## Applications
- Maritime safety and collision avoidance
- Autonomous ship navigation
- Marine traffic simulation and control

## Tech Stack
Python, NumPy, TensorFlow, Physics-Informed Neural Networks (PINNs)
