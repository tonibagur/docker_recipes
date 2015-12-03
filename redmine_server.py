from run_container import run_container

config_docker={
    'port_mapping':[['10083', '80']],
    'volume_mapping':[['/home/coneptum/volumes/redmine','/home/redmine/data']],
    'links':[['postgresql-redmine', 'postgresql']],
    'config_templates':[],
    'environment':[['REDMINE_PORT', '10083'], ['DB_NAME','redmine_production'], [' DB_USER', 'redmine'], ['DB_PASS', 'redminepw0']],
    'expose':[],
    'name':'redmine',
    'image':'sameersbn/redmine:3.1.2-1',
}


if __name__=='__main__':
    run_container(config_docker)
