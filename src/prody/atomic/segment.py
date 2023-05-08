# -*- coding: utf-8 -*-
"""This module defines a class to handle segments of atoms in an atom group."""

from numpy import unique

from .subset import AtomSubset

__all__ = ['Segment']

class Segment(AtomSubset):

    """Instances of this class point to atoms with same segment names and
    are generated by :class:`.HierView` class.  Following built-in functions
    are customized for this class:

    * :func:`len` returns the number of chains in the segment.
    * :func:`iter` yields :class:`.Chain` instances.

    Indexing :class:`Segment` instances by a *chain identifier* (:func:`str`),
    e.g. ``A``, returns a :class:`.Chain`."""

    __slots__ = ['_ag', '_indices', '_hv', '_acsi', '_selstr']

    def __init__(self, ag, indices, hv, acsi=None, **kwargs):

        AtomSubset.__init__(self, ag, indices, acsi, **kwargs)
        self._hv = hv

    def __repr__(self):

        n_csets = self._ag.numCoordsets()
        if n_csets == 1:
            return ('<Segment: {0} from {1} ({2} chains, {3} atoms)>'
                    ).format(self.getSegname(), self._ag.getTitle(),
                             self.numChains(), self.numAtoms())
        elif n_csets > 1:
            return ('<Segment: {0} from {1} ({2} chains, {3} atoms; '
                    'active #{4} of {5} coordsets)>').format(
                    self.getSegname(), self._ag.getTitle(), self.numChains(),
                    self.numAtoms(), self.getACSIndex(), n_csets)
        else:
            return ('<Segment: {0} from {1} ({2} chains, {3} atoms; '
                    'no coordinates)>').format(self.getSegname(),
                    self._ag.getTitle(), self.numAtoms(), self.numChains())

    def __str__(self):

        return 'Segment {0}'.format(self.getSegname())

    def __getitem__(self, chid):

        return self.getChain(chid)

    def getSegname(self):
        """Return segment name."""

        return self._ag._getSegnames()[self._indices[0]]

    def setSegname(self, segname):
        """Set segment name."""

        self.setSegnames(segname)

    def numChains(self):
        """Return number of chains."""

        return len(set(self._getChindices()))

    __len__ = numChains

    def getChain(self, chid):
        """Return chain with identifier *chid*."""

        self._hv.getChain(chid, self.getSegname())

    def iterChains(self):
        """Yield chains."""

        get = self._hv._getChain
        for index in unique(self._getChindices()):
            yield get(index)

    __iter__ = iterChains

    def getSelstr(self):
        """Return selection string that selects atoms in this segment."""

        if self._selstr:
            return 'segname {0} and ({1})'.format(self.getSegname(),
                                                        self._selstr)
        else:
            return 'segname {0}'.format(self.getSegname())
