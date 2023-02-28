import pytest

from noyau import *

@pytest.mark.parametrize("rang, resultat_attendu", [(0, 1), (1, 0)])
def test_changer_joueur(rang, resultat_attendu):
   assert changer_joueur(rang) == resultat_attendu