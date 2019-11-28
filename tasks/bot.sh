#!/bin/bash

echo 'Scheduling a single bot now...'
BOT_RUN=$HOME/Documents/github/com.geodb.location.bot/
cd $BOT_RUN
./environment/master_single_to_sql.sh
