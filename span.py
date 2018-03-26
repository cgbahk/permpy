# todo: docstring required
from permpy.permset import PermSet


def span(*args, **kwargs):
    """ span of permutations
    :param args: permutations <class 'permpy.permutation.Permutation'>
    :param kwargs: (only used in purpose of recursion)
    :return: PermuteSet of span of input permutations
    """
    if not kwargs:  # if kwargs empty, mostly in case of initial call
        for arg in args:
            assert len(args[0]) == len(arg)  # assert same size input
        return span(new=args, old=())  # args is tuple (hashable)
    else:
        new_perms = PermSet(kwargs['new'])
        old_perms = PermSet(kwargs['old'])

        # base case
        if not new_perms:  # if empty
            return old_perms

        # recursion case
        next_old = kwargs['old'] + kwargs['new']
        next_new = ()

        checklist = []  # list of pairs (a,b), which will be computed as a*b
        for new in new_perms:
            for old in old_perms:
                checklist.append((new, old))
                checklist.append((old, new))
        for new1 in new_perms:
            for new2 in new_perms:
                checklist.append((new1, new2))

        # check all checklist, and add if not in old
        for pair in checklist:
            product = pair[0] * pair[1]
            if product not in next_old + next_new:
                next_new += (product,)
        return span(new=next_new, old=next_old)
