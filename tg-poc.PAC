function FindProxyForURL(url, host) {
    // Check for exempted domains
    if (dnsDomainIs(host, "sso.duosecurity.com") || // Matches all *.sso.duosecurity.com
        shExpMatch(host, "thaiairways.login.duosecurity.com") || // Exact match for thaiairways.login.duosecurity.com
        dnsDomainIs(host, "duosecurity.com")) { // Matches all *.duosecurity.com
        return "DIRECT";
    }

    // Default proxy for all other URLs
    return "PROXY turbo-p7p6fqxr.edge.prod.fortisase.com:11491; DIRECT";
}
