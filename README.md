# HydroneLLMStudy

This repository contains the control scripts and study materials for evaluating LLM-driven character personalities on the Hydrone aquatic robot.

This repository accompanies the paper:

> **Character-Driven Personality for an Aquatic Social Robot: A Controlled Study Comparing LLM and Human Puppeteering**
> Ensafjoo et al., *International Journal of Social Robotics* (2026)
> Metropolitan University, Toronto · Edinburgh Napier University · University of Toronto

---

## Related Repository

This study builds on the LLM pipeline first introduced in:

> **Winnie-the-Pooh-Powered: How LLMs and Well-Known Characters Can Create Adaptive Personalities for Aquatic Social Robot Interactions**
> HRI 2026, Edinburgh, Scotland
> 📁 [HydroneLLMScripts](https://github.com/Hydrone-Watercraft/HydroneLLMScripts)

---

## What This Repository Contains

| File | Description |
|---|---|
| `generate_scripts.py` | Prompts GPT-5 to generate motion scripts for each character/scenario combination |
| `joystick_controller.py` | Controls Hydrone in real time via a Logitech Extreme 3D Pro joystick; also triggers LLM-generated scripts via hardware buttons |
| `prompts_water_drone/Hydrone_prompt_basic.txt` | Base prompt describing Hydrone's hardware constraints and command format |
| `README.md` | This file |
| `.gitignore` | Excludes API keys and generated scripts from version control |

> **Note:** The `config.json` file (API key) and `LLM_Generated_Character_Scripts/` folder (generated scripts) are not included in this repository for security reasons. See setup instructions below.

> **Note on firmware:** The onboard firmware that runs on the M5Stack ATOM S3 microcontroller (handling UDP discovery, the TCP command server, the auto-stabilizer, and magnetometer calibration) is not included in this repository.

---

## Characters and Scenarios

Three characters from the Winnie-the-Pooh stories (public domain since 2024) are used as personality archetypes:

| Key | Character | Personality |
|---|---|---|
| `pooh` | Winnie the Pooh | Gentle, curious, moderate |
| `tigger` | Tigger | Bouncy, energetic, enthusiastic |
| `eeyore` | Eeyore | Slow, gloomy, reserved |

Each character is evaluated in two interaction scenarios:

- **Friendly user** — a person approaches Hydrone in a welcoming manner
- **Unfriendly user** — a person approaches Hydrone in an aggressive or startling manner

---

## Study Design

- **Participants:** N = 25 (Mean Age = 26.24)
- **Design:** 3 × 2 × 2 within-participant (3 Characters × 2 Controllers × 2 Scenarios)
- **Controllers compared:** Human puppeteer (40+ years performing arts experience) vs. LLM-generated scripts
- **Evaluation:** Character recognition accuracy, character rating fidelity, and emotional expression via standardized video clips
- **No audio:** Participants evaluated personality solely from body movement and water spray

---

## Hardware

- **Robot platform:** Hydrone (differential propulsion + controllable water pump)
- **Microcontroller:** M5Stack ATOM S3 (ESP32-based, running MicroPython)
- **Communication:** Wi-Fi TCP over local network
- **Joystick:** Logitech Extreme 3D Pro
- **Pool size used in the prompt:** 2 m × 2 m square

Hydrone receives JSON-formatted commands over TCP:

```json
{"left": 20, "right": 20, "pump": 80}
```

- `left` / `right`: thruster power (–30 to +30)
- `pump`: water output duty cycle (30 = off to 100 = max). Values below 30 do not produce any water output, so 30 is treated as the effective "off" value.

---

## Setup

### 1. Install dependencies

```bash
pip install openai pygame
```

### 2. Add your OpenAI API key

Create a `config.json` file in the project root:

```json
{
  "OPENAI_API_KEY": "your-api-key-here"
}
```

> ⚠️ Never share or commit this file. It is listed in `.gitignore` and excluded from this repository.

### 3. Connect your joystick

Plug in the Logitech Extreme 3D Pro before running the controller.

### 4. Set your device name

In `joystick_controller.py`, update `TARGET_NAME` to match your Hydrone's device name:

```python
TARGET_NAME = "atom_s3_1"   # change to your device name
```

---

## Usage

### Generate LLM motion scripts

```bash
python generate_scripts.py
```

An interactive menu lets you generate scripts for individual character/scenario pairs or all six at once. Scripts are saved to `LLM_Generated_Character_Scripts/`.

```
---- Hydrone Emotion Script Generator ----
1. Pooh    - Friendly
2. Pooh    - Unfriendly
3. Tigger  - Friendly
4. Tigger  - Unfriendly
5. Eeyore  - Friendly
6. Eeyore  - Unfriendly
7. Generate All
0. Exit
```

### Run the joystick controller

```bash
python joystick_controller.py
```

The script will auto-discover Hydrone on the local network via UDP broadcast, then connect over TCP. Once connected:

| Control | Action |
|---|---|
| Main stick (axis 2) | Forward / backward |
| Main stick (axis 1) | Rotate left / right |
| D-pad up / down | Forward / backward |
| D-pad left / right | Rotate left / right |
| Trigger (button 0) | Pump 100% |
| Thumb (button 1) | Pump off |
| Knob (axis 3) | Pump 0–100% |
| Buttons 6–11 | Run pre-generated LLM character script |
| Button 2 | Exit |

---

## LLM Script Button Mapping

Buttons 6–11 trigger pre-generated scripts from the `LLM_Generated_Character_Scripts/` folder:

| Button | Script |
|---|---|
| 6 | pooh_friendly.py |
| 7 | pooh_unfriendly.py |
| 8 | tigger_friendly.py |
| 9 | tigger_unfriendly.py |
| 10 | eeyore_friendly.py |
| 11 | eeyore_unfriendly.py |

---

## Citation

If you use this code in your research, please cite:

```bibtex
@article{ensafjoo2026hydrone,
  title   = {Character-Driven Personality for an Aquatic Social Robot:
             A Controlled Study Comparing LLM and Human Puppeteering},
  author  = {Ensafjoo, Mohsen and Nguyen, Chau and Hoss, Jordan and
             Li, Jamy and Dietz, Paul H. and Mazalek, Ali},
  journal = {International Journal of Social Robotics},
  year    = {2026}
}
```
