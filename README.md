# DayZ Player Count Bot

## Overview

A Python bot that monitors and logs the player count of a DayZ server every 5 minutes.

## Features
- Lightweight
- Queries DayZ server every 5 minutes
- Logs player count with timestamps
- Configurable settings via `.env` file

## Configuration

Edit the `.env` file in the root directory:

```dotenv
SERVER_IP=your.dayz.server..query.ip
SERVER_PORT=2302
DISCORD_TOKEN = fa676fa6yayyd62

```
## Installation

```
pip install -r requirements.txt
```

## Run Bot

```
Python bot.py
```
