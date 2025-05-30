"""Create dish table

Revision ID: a53cb978eb5c
Revises: 1392c47815bf
Create Date: 2025-04-25 14:43:42.257808

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a53cb978eb5c"
down_revision: Union[str, None] = "1392c47815bf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "dishes",
        sa.Column("title", sa.String(length=50), nullable=False),
        sa.Column("category", sa.Integer(), nullable=False),
        sa.Column(
            "description",
            sa.Text(),
            server_default="",
            nullable=True,
        ),
        sa.Column(
            "composition",
            sa.String(length=150),
            server_default="",
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), sa.Identity(always=True), nullable=False),
        sa.ForeignKeyConstraint(["category"], ["categories.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_dishes_title"), "dishes", ["title"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_dishes_title"), table_name="dishes")
    op.drop_table("dishes")
    # ### end Alembic commands ###
