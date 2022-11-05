from github_api import GitHub

if __name__ == '__main__':
    # Connection object
    gh = GitHub(
        api_key='')

    # Repository
    repo = gh.get_repository('isc-projects', 'bind9')

    # Releases
    releases = repo.get_releases()
    tags = repo.get_tags()
