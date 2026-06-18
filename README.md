# Portfolio Project Structure & Supported Formats

This portfolio automatically discovers projects placed inside the `projects/` directory.

## Adding a New Project

Create a new folder inside `projects/`:

```text
projects/
└── My-Robot-Project/
    ├── index.md
    ├── featured.jpg
    ├── gallery/
    ├── models/
    ├── schematics/
    ├── diagrams/
    ├── code/
    └── data/
```

No additional configuration is required.

The website automatically detects:

* Project information
* Featured image
* Gallery media
* 3D models
* Circuit schematics
* Technical diagrams
* Code files
* CSV datasets

---

# Required Files

## index.md

Every project must contain an `index.md` file.

Example:

```markdown
---
layout: project
title: "Vision-Based Autonomous Mobile Robot"
description: "Autonomous tracked robot using computer vision and ESP32."
date: 2026-01-01
categories: [Robotics, Mechatronics, Embedded Systems]
github_url: ""
---

Project description goes here.

## Overview

Explain the project.

## Specifications

| Component | Details |
|-----------|---------|
| Controller | ESP32 |
| Sensors | MPU6050, Ultrasonic |
| Communication | WiFi |
```

---

# Featured Image

The project thumbnail is automatically loaded from:

```text
featured.jpg
```

Supported formats:

```text
featured.jpg
featured.jpeg
featured.png
featured.webp
```

Recommended:

```text
1200 × 800 pixels
```

---

# Gallery

Place media inside:

```text
gallery/
```

Supported image formats:

```text
.jpg
.jpeg
.png
.webp
.gif
```

Supported video formats:

```text
.mp4
.webm
.mov
```

Example:

```text
gallery/
├── image1.jpg
├── image2.png
├── demo.gif
├── assembly.mp4
└── testing.webm
```

All files are automatically displayed in the gallery.

---

# 3D Models

Place 3D files inside:

```text
models/
```

Supported formats:

```text
.glb
.gltf
.stl
.obj
```

Recommended:

```text
.glb
```

Example:

```text
models/
├── robot.glb
├── gripper.glb
└── chassis.stl
```

All models are automatically detected and displayed.

---

# Schematics

Place electrical diagrams inside:

```text
schematics/
```

Supported formats:

```text
.svg
.png
.jpg
.jpeg
.webp
```

Example:

```text
schematics/
├── wiring.svg
├── pcb.png
└── circuit.jpg
```

---

# Technical Diagrams

Place system diagrams inside:

```text
diagrams/
```

Supported formats:

```text
.svg
.png
.jpg
.jpeg
.webp
.pdf
```

Example:

```text
diagrams/
├── system-architecture.svg
├── workflow.png
└── block-diagram.pdf
```

---

# Code Files

Place source code inside:

```text
code/
```

Supported formats:

```text
.py
.cpp
.c
.h
.hpp
.ino
.js
.ts
.html
.css
.scss
.java
.cs
.m
.mlx
.ipynb
```

Example:

```text
code/
├── main.cpp
├── vision.py
└── navigation.ino
```

---

# Data Files

Place datasets inside:

```text
data/
```

Supported formats:

```text
.csv
.txt
.json
.xml
```

Example:

```text
data/
├── sensor_data.csv
├── battery_log.csv
└── performance.json
```

CSV files can be used for charts and interactive visualizations.

---

# Project Categories

Examples:

```yaml
categories:
  - Robotics
  - Mechatronics
  - Embedded Systems
  - Computer Vision
  - Automation
  - IoT
  - AI
  - Electronics
  - Mechanical Design
  - Control Systems
```

---

# Complete Example

```text
projects/
└── Vision-Based-Mobile-Robot/
    ├── index.md
    ├── featured.jpg
    ├── gallery/
    │   ├── robot.jpg
    │   ├── testing.jpg
    │   └── demo.mp4
    ├── models/
    │   ├── chassis.glb
    │   └── arm.glb
    ├── schematics/
    │   └── wiring.svg
    ├── diagrams/
    │   └── architecture.png
    ├── code/
    │   ├── main.cpp
    │   └── vision.py
    └── data/
        └── results.csv
```

Adding a new project only requires creating a new folder inside `projects/` and placing the files in the appropriate subfolders.
