FROM lucone83/streamlit-nginx:python3.8

USER root

COPY docker/demo/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --no-cache-dir

USER streamlitapp

COPY --chown=streamlitapp src/demo /home/streamlitapp/deep-metal

CMD ["streamlit", "run", "deep-metal/deep_metal.py", "deep-metal"]
