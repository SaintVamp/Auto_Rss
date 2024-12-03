git pull
cp /auto_rss/model_config/model-config.toml /auto_rss/config/.
python3 run_rss.py &
sleep 30s
while true; do
  if [ -f /auto_rss/upgrade ]; then
    git pull
    cp /auto_rss/model_config/model-config.toml /auto_rss/config/.
    ps | grep "python3 run_rss.py" | grep -v grep | awk '{print $1}' | xargs kill -9
    python3 run_rss.py &
    rm /auto_rss/upgrade
  fi
  sleep 5m
done