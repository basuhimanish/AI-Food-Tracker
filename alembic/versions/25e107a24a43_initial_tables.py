"""initial tables

Revision ID: 25e107a24a43
Revises: 256e687bfecb
Create Date: 2025-08-07 14:32:08.497509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25e107a24a43'
down_revision: Union[str, None] = '256e687bfecb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
