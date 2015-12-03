from run_container import run_container

config_docker={
    'port_mapping':[],
    'volume_mapping':[['/home/coneptum/redmine/volumes','/var/lib/postgresql']],
    'links':[],
    'config_templates':[],
    'environment':[['DB_NAME','redmine_production'], [' DB_USER', 'redmine'], ['DB_PASS', 'redminepw0'], ['POSTGRES_PASSWORD', 'redminepw0']],
    'expose':[],
    'name':'postgresql-redmine',
    'image':'sameersbn/postgresql:9.4-8',
}


if __name__=='__main__':
    run_container(config_docker)
