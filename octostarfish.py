
import logging
import sys

from .query_gists import query_gists
from .query_stars import query_stars


logger = logging.getLogger(__name__)


class Octostarfish(object):
    """Expose all public functionality.
    Use `Octostarfish.run()` to kick things off!
    """
    @classmethod
    def run(cls, user, token, clones_root):
        """Run the Octostarfish job."""
        logger.info('Starting')
        fish = cls(user, token)
        logger.info('Starting to pull starred repositories')
        for repo in fish.starred_repos():
            try:
                fish.clone(repo, clones_root)
            except Exception:
                logger.exception('Error pulling {0}'.format(repo.gh_path))
        logger.info('Starting to pull starred gists')
        for repo in fish.starred_gists():
            try:
                fish.clone(repo, clones_root)
            except Exception:
                logger.exception('Error pulling {0}'.format(repo.gh_path))
        logger.info('Done')

    def __init__(self, user, token):
        if user is None:
            sys.stderr.write(
                'You must specify a user with --user or the GITHUB_USER '
                'environment variable.\n')
            sys.exit(1)
        if token is None:
            sys.stderr.write(
                'You must specify a token with --token or the '
                'GITHUB_API_TOKEN environment variable.\n')
            sys.exit(1)
        self.user = user
        self.token = token

    def clone(self, repo, clones_root):
        """Manage a clone of a given repository.
        Positional arguments:
        repo - An octostarfish.repo.Repo.
        clones_root - A path-like object one level representing the parent
            directory of the clone.
        """
        repo.clone(clones_root / repo.gh_path)

    def starred_gists(self):
        """Retrieve the user's starred gists
        Returns a sequence of octostarfish.repo.Repos.
        """
        return query_gists(self.user, self.token)

    def starred_repos(self):
        """Retrieve the user's starred repositories.
        Returns a sequence of octostarfish.repo.Repos.
        """
        return query_stars(self.user, self.token)