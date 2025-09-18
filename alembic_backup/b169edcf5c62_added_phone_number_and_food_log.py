"""added phone number and food log

Revision ID: b169edcf5c62
Revises: 25e107a24a43
Create Date: 2025-08-07 14:34:12.732736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b169edcf5c62'
down_revision: Union[str, None] = '25e107a24a43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
