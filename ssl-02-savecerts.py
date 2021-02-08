
der_certs = ctx.get_ca_certs(binary_form=True)
pem_certs = [ssl.DER_cert_to_PEM_cert(der_cert_bytes) for der_cert_bytes in der_certs]
tmpcert = '\n'.join(pem_certs) 

f = open('tmpcert.pem','w')
f.write(tmpcert)
f.close()
