import ldap3

class LDAPSource(object):
    def __init__(self, server, bindas, passwd):
        server = ldap3.Server(server)
        self.conn = ldap3.Connection(server, read_only=True,
                                     user=bindas, password=passwd,
                                     auto_bind=ldap3.AUTO_BIND_TLS_AFTER_BIND)

    def get_hostsinfo(self, project):
        self.conn.search('ou=hosts,dc=wikimedia,dc=org',
                         '(puppetVar=instanceproject=%s)' % project,
                         ldap3.SEARCH_SCOPE_WHOLE_SUBTREE,
                         attributes=ldap3.ALL_ATTRIBUTES)
        hosts = []
        for responseitem in self.conn.response:
            hostinfo = responseitem['attributes']
            ip = [a for a in hostinfo['aRecord'] if a.startswith('10.')][0]
            puppetvars = {var[0]: var[1] for var in [pv.split("=") for pv in hostinfo['puppetVar']]}
            hosts.append({
                'ec2id': hostinfo['dc'][0],
                'ip': ip,
                'region': hostinfo['l'][0],
                'puppetClasses': hostinfo['puppetClass'],
                'project': project,
                'name': puppetvars['instancename'],
                'puppetVars': puppetvars
            })

        return hosts
