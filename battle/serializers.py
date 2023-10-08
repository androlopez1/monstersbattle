from rest_framework import serializers

from battle.models import Battle
from monster.models import Monster

from .utils import fight


class BattleListSerializer(serializers.ModelSerializer):
    monsterA = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    monsterB = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    winner = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = Battle
        fields = "__all__"


class BattleCreateSerializer(serializers.ModelSerializer):
    # monsterA = MonsterListRetrieveUpdateSerializer(write_only=True)
    # monsterB = MonsterListRetrieveUpdateSerializer(write_only=True)
    monsterA = serializers.PrimaryKeyRelatedField(
        queryset=Monster.objects.all(),
        write_only=True,
    )
    monsterB = serializers.PrimaryKeyRelatedField(
        queryset=Monster.objects.all(),
        write_only=True,
    )
    winner = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = Battle
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        monster_a = validated_data["monsterA"]
        monster_b = validated_data["monsterB"]

        winner = fight(monster_a, monster_b)

        battle = Battle.objects.create(
            monsterA=monster_a.id,
            monsterB=monster_b.id,
            winner=winner.id,
        )

        return battle
