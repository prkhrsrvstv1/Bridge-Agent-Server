# Bridge-Agent-Server

## Local Testing

```shell
# Git clone and cd into the repo directory
git clone https://github.com/prkhrsrvstv1/Bridge-Agent-Server.git

# Start using the packaged Python venv
./venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the local server with auto-reload enabled
uvicorn main:app --reload
```