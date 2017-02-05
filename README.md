# OpenHealth

OpenHealth is a a decentralized application that connects patient records stored at different hospitals, allowing patients to securely transfer their medical records between health professionals.  It uses blockchain technology to control access to hospitals' databases, so that no one can manipulate or change any records without leaving an trail behind. 


# Installation

To install, first install the embark framework (stop at the Usage - Demo title in the embark README)

https://github.com/iurimatias/embark-framework#installation


# Run 

Run a REAL etherum node for development purposes:

```Bash
$ embark blockchain
```

Then, in another terminal window, run:

```Bash
$ embark run
```

To run server in command line:

```Bash
$ make server
```

# NOTE

Users can run into some compatibility issues if they are using node version 4.0.0 or lower. Upgrade Node to the latest version and uninstall any old versions to avoid conflicts.
