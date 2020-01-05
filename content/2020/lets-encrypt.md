title: https troubleshooting
tags: code
date: 2020-01-05


My Let's Encrypt certificate was failing to renew. I had assigned it to a handful of domains when it was generated and one of those domains expired, causing the verification challenge to fail.

I tried to generate a new certificate without the expired domain, but kept getting malformed request errors. I honestly don't remember how long ago I first set it up, so I thought that maybe my installed version of certbot was out of date.

After updating cerbot, I was able to generate a new certificate, but when I tried to reach the domain using a web browser, the browser refused to connect becuase a secure connection couldn't be established.

Not sure where to go next, I decided to spin up a new droplet and migrate. This had the added benefit of upgrading to Ubuntu 18.04 TLS.

I re-created my nginx configuration for curtmerrill.com and used certbot's `certonly` option to request a new certificate. I specified only one domain this time so I'll need to generate new certificates for the other domains.

I still need to migrate the other sites to the new droplet and generate certificates for the domains, but if you're reading this, it means I was successful in getting curtmerrill.com back up.
