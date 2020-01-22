# Serving Tensorboard UI on startup

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/tensorboard/master?urlpath=%2fproxy%2f6006%2f) (Tensorboard)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/binder-examples/tensorboard/master?filepath=train_model.ipynb) (notebook)

An example of running Jupyter notebook + tensorboard on mybinder.org. To launch tensorboard go to:

https://mybinder.org/v2/gh/btel/binder-tensorboard/master?urlpath=%2fproxy%2f6006%2f

This example shows how to:

* expose the [tensorboard](https://www.tensorflow.org/tensorboard/) interface on
  binder,
* use the
  [jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy)
  extension to map a web application running on a port inaccessible from the
  internet (6006 for example) to jupyter path (`/proxy/6006/`),
* launch tensorboard on startup using the custom server extension
  (`tensorboardserverextension.py`).

## Notes

Once the tensorboard is launched you can also open and run the notebooks by replacing
the `/proxy/6006/` part of the URL (or everything after `/proxy`) with `/tree`
(or `/lab` for jupyter lab view).

When you run the training of the neural net in the notebook you can watch the
progress of the run live (you can keep tensorboard open in a separate tab). 

## How?

tensorboard launches a webserver on a given port (by default 6006). In many
environments (like dockerized deployments), the port is not visible in the
external network. To expose it, we use the jupyter-servery-proxy extension to proxy it
to the jupyter server URL (`/proxy/6006/`, mind the [trailing
slash](https://github.com/jupyterhub/jupyter-server-proxy/issues/41`)!)

The `tensorboardserverextension.py` file, which is executed by jupyter server on
start up, launches the tensorboard server.
