"""add_disabled_field_to_action_event

Revision ID: a29b537fabe6
Revises: 98c8851a5321
Create Date: 2024-05-28 11:28:50.353928

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "a29b537fabe6"
down_revision = "98c8851a5321"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("action_event", schema=None) as batch_op:
        batch_op.add_column(sa.Column("disabled", sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("action_event", schema=None) as batch_op:
        batch_op.drop_column("disabled")

    # ### end Alembic commands ###
