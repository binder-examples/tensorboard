[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/btel/binder-tensorboard/master?urlpath=%2fproxy%2f6006%2f)

An example of running Jupyter notebook + tensorboard on mybinder.org. To launch tensorboard go to:

https://mybinder.org/v2/gh/btel/binder-tensorboard/master?urlpath=%2fproxy%2f6006%2f

Once the tensorboard is launched you can also see the notebooks by replacing the /proxy/6006/ part of the URL (or everything after `/proxy`) with `/tree` (or `/lab` for jupyter lab view).

When you run the notebook you can see the progress of the run live! You can see it either in a separate tab of your browser or the embedded view in the notebook.

## How?

tensorboard launches a webserver on a given port (by default 6006). In many environments (like dokerized deployments), the port is not visible in the external network. To expose, we use the jupyter-proxy-extension to proxy it to the jupyter server url (`/proxy/6006`)

The `tensorboardserverextension.py` file, which is run by jupyter server on start up, is responsible for launching the tensorboard server.
