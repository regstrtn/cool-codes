## For running a remote server 

### On Client Machine
1. Create a ssh tunnel 
`ssh -N -f -L localhost:8881:localhost:9876 user@address.of.server`

2. In your web browser, type this: `localhost:8881`


### On Server
`jupyter notebook --ip=localhost --no-browser --port=9876`

#### To enable password, run this on terminal

`$jupyter notebook --generate-config`

`$jupyter notebook password`
