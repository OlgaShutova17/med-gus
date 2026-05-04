---
title: Figma — промпт для дизайна мобильного приложения
---

Готовый промпт для Figma AI (Make Designs / Figma AI / Anima). Вставить как есть в поле промпта.

---

## ПРОМПТ

```
Design a mobile health investigation app called "МедДневник" (MedDnevnik).
App mascot: a friendly white goose named "Гусик" (Gusik) wearing a small
doctor's mirror on his forehead and a tiny stethoscope. He appears in empty
states, onboarding, loading screens, and as the AI assistant avatar.

The app helps users investigate health problems using the model:
Problem → Hypotheses → Events → Evidence → Resolution.

Platform: iOS/Android (React Native). Design for iPhone 14 Pro (390×844pt).

═══════════════════════════════════════════
DESIGN SYSTEM
═══════════════════════════════════════════

STYLE
Clean medical minimalism with warmth. The sea-wave teal palette conveys
trust, calm, and health — not cold clinical blue. Gusik mascot adds
approachability to a serious medical context.

GRID
4-column, 16px margins, 8px gutter. 8pt baseline grid throughout.
Safe area: 59pt top (Dynamic Island), 34pt bottom (home indicator).

─────────────────────────────────────────
COLOR PALETTE — "Морская волна" (Sea Wave)
─────────────────────────────────────────

Background:       #F0FDFA  (teal-50, main screen bg)
Surface:          #FFFFFF  (cards, bottom sheets, modals)
Surface Alt:      #F0FDFA  (subtle section backgrounds)

Primary:          #0D9488  (teal-600 — actions, active states, buttons)
Primary Dark:     #0F766E  (teal-700 — pressed states)
Primary Light:    #CCFBF1  (teal-100 — selected backgrounds, tints)
Primary Tint:     #F0FDFA  (teal-50 — AI card backgrounds)

Accent:           #06B6D4  (cyan-500 — highlights, progress bars, charts)
Accent Light:     #CFFAFE  (cyan-100 — accent tints)

Success:          #16A34A  (green-600 — normal values, "Helped", confirmed)
Success Light:    #DCFCE7  (green-100)
Warning:          #D97706  (amber-600 — deviations, testing status)
Warning Light:    #FEF3C7  (amber-100)
Danger:           #DC2626  (red-600 — critical values, "Not helped", rejected)
Danger Light:     #FEE2E2  (red-100)

Text Primary:     #134E4A  (teal-900 — main text, dark on white)
Text Secondary:   #6B7280  (gray-500 — metadata, captions, placeholders)
Text On Primary:  #FFFFFF  (white — text on teal buttons)

Border:           #CCFBF1  (teal-100 — card borders, dividers)
Border Strong:    #99F6E4  (teal-200 — input borders active)
Divider:          #F0FDFA  (teal-50 — section separators)

Shadow: 0px 1px 3px rgba(13, 148, 136, 0.08), 0px 1px 2px rgba(13, 148, 136, 0.04)

─────────────────────────────────────────
TYPOGRAPHY
─────────────────────────────────────────

Font: Inter (iOS fallback: SF Pro)

H1:       24px / 700 / -0.3 letter-spacing  (screen titles)
H2:       18px / 600 / -0.2                 (card titles, section headers)
H3:       16px / 600                         (list item titles)
Body:     15px / 400 / 1.5 line-height       (main content)
Body Med: 15px / 500                         (emphasized body)
Caption:  13px / 400 / 1.4                  (dates, labels, meta)
Mono:     14px / 500 / tabular nums          (medical values, numbers)
Micro:    11px / 500 / uppercase 0.5 tracking (badges, tags)

─────────────────────────────────────────
STATUS BADGES
─────────────────────────────────────────

new:        #F0FDFA bg / #0D9488 text / "Новая"
testing:    #FEF3C7 bg / #D97706 text / "Проверяется"
confirmed:  #DCFCE7 bg / #16A34A text / "Подтверждена"
rejected:   #FEE2E2 bg / #DC2626 text / "Отклонена"
helped:     #DCFCE7 bg / #16A34A text / "Помогло"
not_helped: #FEE2E2 bg / #DC2626 text / "Не помогло"
active:     #CCFBF1 bg / #0F766E text / "Активная"
resolved:   #F0FDFA bg / #6B7280 text / "Завершена"

Badge shape: rounded, 4px radius, 4px vertical / 8px horizontal padding.
Micro font (11px / 500 / uppercase).

─────────────────────────────────────────
VALUE STATUS INDICATORS
─────────────────────────────────────────

Normal:   #16A34A dot + green text + "↔ норма"
Low:      #D97706 dot + amber text + "↓ ниже нормы"
High:     #D97706 dot + amber text + "↑ выше нормы"
Critical: #DC2626 dot + red bold text + "↓↓ критично" + background flash

─────────────────────────────────────────
MASCOT — ГУСИК (Gusik the Goose)
─────────────────────────────────────────

Character description:
- White round-bodied goose, friendly expression, large eyes
- Accessory 1: small circular doctor's mirror (frontoscope) on forehead, gold-rimmed
- Accessory 2: tiny stethoscope around neck in teal (#0D9488)
- Beak: warm orange (#FB923C)
- Feet: same orange, slightly visible
- Style: flat illustration, gentle shadows, friendly not cartoonish
- Sizes: 120pt (onboarding full), 64pt (empty states), 32pt (AI avatar), 24pt (inline icon)

Gusik variants:
  GUSIK_WAVE:     waves with wing, smiling — onboarding welcome
  GUSIK_THINK:    wing on chin, thoughtful look — loading / AI processing
  GUSIK_HAPPY:    wings spread, very happy — success states
  GUSIK_SEARCH:   magnifying glass in wing — empty states "nothing found"
  GUSIK_DOCTOR:   clipboard in wing, professional stance — AI assistant avatar
  GUSIK_SLEEP:    eyes closed, ZZZs — onboarding screen 1

Gusik usage rules:
- Always centered horizontally in empty states
- Caption below mascot in Text Secondary color
- Never use mascot on screens with critical health alerts
- AI assistant always uses GUSIK_DOCTOR at 32pt in message bubbles

─────────────────────────────────────────
COMPONENT LIBRARY
─────────────────────────────────────────

1. ThemeCard
   White card, 16px padding, 12px radius, teal border (#CCFBF1), shadow.
   - Color stripe left edge: 4px wide, Primary color (#0D9488)
   - Title (H2, Text Primary)
   - Leading hypothesis chip: teal-100 bg, teal text, "Дефицит железа · 72%"
   - Row: status badge LEFT + last event date caption RIGHT
   - Events count: "5 событий" (Caption, Secondary)
   States: Default / Pressed (scale 0.98, shadow reduced) / Skeleton loading

2. EventCard
   White card, 16px padding, 12px radius, shadow.
   - Header row: [TypeIcon 32pt colored circle] + [Title H3] + [Date Caption right]
   - TypeIcon colors by event type:
       Анализ:       #CCFBF1 bg / #0D9488 icon  (flask)
       Консультация: #CFFAFE bg / #06B6D4 icon  (person with cross)
       Исследование: #EDE9FE bg / #7C3AED icon  (scan/layers)
       Другое:       #F3F4F6 bg / #6B7280 icon  (file-text)
   - Value rows (for analyses only): ParameterRow component × N
   - Hypothesis impact row: "Влияние:" + EvidenceChip × N
   - Resolution area: two outlined buttons (see ResolutionButton)
   States: Default / Expanded / With resolution set

3. HypothesisCard
   White card, 16px padding, 12px radius, left border 4px by status color.
   - Header: [Title H2] + [StatusBadge right]
   - ConfidenceBar: full width, teal fill (color by confidence %)
   - "Подтверждения:" section: EvidenceChip (green) × N
   - "Опровержения:" section: EvidenceChip (red) × N, or "—"
   - Footer row: text link "Подробнее →"
   States: Default / Expanded / Confirmed (green left border) / Rejected (red)

4. ParameterRow
   Full width, 44pt height, no card (table row style).
   - Parameter name (Body, Text Primary) LEFT
   - [ValueDot] [Value Mono colored] [Unit Caption] CENTER
   - Reference range "20–150 мкг/л" (Caption Secondary) RIGHT
   Status dot: 6pt circle, colored by value status.

5. AIInsightCard
   Background: Primary Tint (#F0FDFA), border: 1px #CCFBF1, 12px radius.
   - Header row: [GUSIK_DOCTOR 32pt] + "Гусик говорит" (Caption, Primary)
   - Insight text (Body)
   - Disclaimer: "Не является медицинским заключением" (Caption Secondary, italic)
   - "Подробнее →" teal link right

6. StatusBadge — 8 variants per palette above.

7. ValueChip — inline tag: colored dot + value + status text.

8. EvidenceChip
   Supports: #DCFCE7 bg / #16A34A text / "✓" prefix
   Rejects:  #FEE2E2 bg / #DC2626 text / "✗" prefix
   Neutral:  #F3F4F6 bg / #6B7280 text / "–" prefix
   Shape: pill, 6px radius, 4px/10px padding.

9. ConfidenceBar
   Full width bar, 8pt height, 4px radius.
   Track: #CCFBF1. Fill: color by value:
     0–30%: #D97706 (low confidence)
     31–60%: #06B6D4 (moderate)
     61–100%: #0D9488 (high)
   Label above right: "72%" (Mono, colored matching fill)

10. ResolutionButton — two variants side by side:
    Helped:     outlined #16A34A border+text, icon ✓
    Not helped: outlined #DC2626 border+text, icon ✗
    Selected helped:     filled #16A34A, white text, locked
    Selected not helped: filled #DC2626, white text, locked
    Height: 40pt, flex 1 each, 8px gap between.

11. FAB — 56pt circle, Primary (#0D9488), white "+" icon 24pt, shadow.
    Positioned: bottom 24pt + safe area, right 20pt.

12. BottomSheet
    White, top 16px radius, handle bar 4×32pt centered 8pt from top.
    Max height: 80vh. Drag to dismiss.

13. EmptyState
    Centered vertically in container.
    [Gusik variant 64pt] + Title H2 + Body text + Optional CTA button.

14. TabBar (custom, inside screen)
    Horizontal, full width, 44pt height.
    Active tab: Text Primary + Primary underline 2pt.
    Inactive: Text Secondary.
    Background: white. Bottom border: #CCFBF1.

15. BottomNavBar
    5 tabs: Главная / Проблемы / + (FAB) / Аналитика / Профиль
    Center tab "+" is elevated FAB style: 56pt circle Primary, raised 12pt.
    Active icon+label: Primary color. Inactive: Text Secondary.
    Background: white. Top border: #CCFBF1. Height: 83pt (with safe area).

16. InputField
    Height: 52pt, 12px radius, border 1.5px #CCFBF1.
    Focus: border #0D9488, subtle teal glow 0 0 0 3px #CCFBF1.
    Error: border #DC2626, error text below in Danger color.
    Label: floats above on focus (13px Caption, Primary).

17. PrimaryButton — full width, 52pt height, 12px radius, Primary bg.
    Label: 16px/600, white. Press: Primary Dark bg.

18. SecondaryButton — outlined, Primary border+text, transparent bg.

═══════════════════════════════════════════
SCREEN 1 — ONBOARDING (3 slides)
═══════════════════════════════════════════

Background: gradient top-to-bottom #F0FDFA → #CCFBF1.
Bottom sheet fixed: white, 360pt height, 24px top radius.

SLIDE 1 — "Привет, я Гусик!"
  Top area (illustration zone):
    GUSIK_SLEEP centered, 120pt, teal medical mirror glowing faintly
  Bottom sheet:
    H1: "Привет, я Гусик!"
    Body: "Я помогу разобраться — почему тебе плохо.
           Не просто хранить анализы, а найти причину."
    Pagination dots: 3 dots, active = Primary, inactive = #CCFBF1

SLIDE 2 — "Веди расследование"
  Top area: illustration of teal phone screen with timeline + hypothesis cards
  Bottom sheet:
    H1: "Веди расследование"
    Body: "Добавляй события, строй гипотезы.
           Смотри — что подтверждает причину, а что опровергает."

SLIDE 3 — "Начнём?"
  Top area: GUSIK_WAVE, 120pt, large happy pose
  Bottom sheet:
    H1: "Начнём?"
    Body: "Создай первую тематику и добавь свою проблему."
    [Зарегистрироваться] — PrimaryButton
    [Уже есть аккаунт — войти] — text link, Primary color, below button

═══════════════════════════════════════════
SCREEN 2 — REGISTRATION / LOGIN
═══════════════════════════════════════════

Background: #F0FDFA.

Top: GUSIK_DOCTOR 48pt + "МедДневник" wordmark (H1, Primary) horizontally centered.
Tagline: "Твой медицинский дневник" (Caption, Secondary).

Toggle tabs: [Регистрация] / [Вход] — full width, 44pt, active tab: Primary bg white text.

REGISTRATION FORM:
  InputField: "Ваше имя"
  InputField: "Email"
  InputField: "Пароль" (with show/hide eye icon)
  Checkbox + link: "Согласен(на) с обработкой персональных данных →"
  [Создать аккаунт] — PrimaryButton, disabled until checkbox checked.

LOGIN FORM:
  InputField: "Email"
  InputField: "Пароль"
  "Забыли пароль?" — text link right-aligned
  [Войти] — PrimaryButton.

═══════════════════════════════════════════
SCREEN 3 — DASHBOARD (главный экран)
═══════════════════════════════════════════

Status bar area. ScrollView content.

HEADER (non-scrolling):
  Left: "Привет, Ольга 👋" (H2, Text Primary)
  Right: notification bell icon (24pt, Secondary), badge if alerts
  Below: "4 мая 2026" (Caption, Secondary)

SECTION: "Мои тематики"
  Row: "Мои тематики" (H2) + "Все →" (Caption, Primary) right
  Horizontal scroll cards or full-width list (max 3 shown):
    ThemeCard × N
    Last item: "+ Новая тематика" card — dashed teal border, centered "+"
  EMPTY STATE: GUSIK_SEARCH 64pt + "Пока нет тематик" + "Создать первую →" button

SECTION: "Последние события" (if any themes exist)
  Compact event list items (not full EventCard):
    [TypeIcon 32pt] | [Title Body Med + "· Тематика" Caption] | [Date Caption right]
  Up to 5 items. "Смотреть все →" link below.
  EMPTY: GUSIK_WAVE 48pt + "Добавь первое событие"

Bottom navigation: BottomNavBar

═══════════════════════════════════════════
SCREEN 4 — CREATE THEME
═══════════════════════════════════════════

Navigation: back arrow (←) + "Новая тематика" (H1 center) + "Отмена" right.

Form (full screen, scroll):
  GUSIK_THINK 48pt at top, centered. Caption below: "Что беспокоит?"
  InputField large: "Название проблемы *"
    Placeholder: "Например: Хроническая усталость"
    Character counter right: "0/100"
  InputField multiline (5 rows): "Описание (необязательно)"
    Placeholder: "Опишите, что происходит, когда началось..."

Bottom (sticky):
  [Создать тематику] — PrimaryButton, disabled until title filled.

═══════════════════════════════════════════
SCREEN 5 — THEME DETAIL (3 вкладки)
═══════════════════════════════════════════

HEADER (non-scrolling, white, shadow):
  Back arrow (←)
  [Theme title H1 + StatusBadge] centered, 2 lines max
  Menu icon (⋮) — Edit / Archive

AI SUMMARY CARD (below header, non-scrolling):
  Background: #F0FDFA, border #CCFBF1, 12px radius, 12px horizontal margin.
  Left: [GUSIK_DOCTOR 32pt]
  Right stack:
    "Гусик думает:" (Caption, Secondary)
    "Дефицит железа" (H2, Primary)
    ConfidenceBar + "72% уверенности"
    "Обновлено 4 мая" (Caption Secondary, right)

TAB BAR (below AI card):
  [ Timeline ] [ Гипотезы ] [ Симптомы ]
  Active: Primary underline 2pt, Text Primary bold.

FAB: bottom-right, "+", Primary.

─────────────────────────────────────────
SCREEN 5A — TIMELINE TAB
─────────────────────────────────────────

ScrollView. Newest first.
Month group headers: "Май 2026" — Caption uppercase, Secondary, with divider line.

EventCard × N (full width, 12px horizontal margin)

EMPTY: GUSIK_SEARCH 64pt + "Пока нет событий"
       "Добавь первое: консультацию, анализ или исследование"
       [Добавить событие] — PrimaryButton (outlines style, teal)

─────────────────────────────────────────
SCREEN 5B — HYPOTHESES TAB
─────────────────────────────────────────

Header row: "Гипотезы" (H2) + [+ Добавить] (text button, Primary) right.
ScrollView.

HypothesisCard × N

EMPTY: GUSIK_THINK 64pt + "Гипотез пока нет"
       "Гипотеза — предполагаемая причина проблемы"
       [Добавить гипотезу] — PrimaryButton outlined.

─────────────────────────────────────────
SCREEN 5C — SYMPTOMS TAB
─────────────────────────────────────────

Header row: "Симптомы" (H2) + [+ Добавить] right.

Symptom chips (wrapping, 8px gap):
  Each chip: white bg, teal border, Text Primary, 8px radius, 8px/16px padding.
  With severity dot (optional): small colored circle before text.
  With remove ×: small × right inside chip, tap to delete.

[+ Добавить симптом] — dashed teal bordered chip, full width.
Bottom sheet on tap: search field + preset list + "Другое" freetext option.

EMPTY: GUSIK_WAVE 64pt + "Добавь симптомы, чтобы Гусик мог помочь"

═══════════════════════════════════════════
SCREEN 6 — ADD EVENT (выбор типа)
═══════════════════════════════════════════

Bottom sheet (slides up, 420pt). BottomSheet component.

Header: "Добавить событие" (H2 center).
Sub: "К тематике: [ThemeName]" — teal chip, tappable to change.

Type grid (2×2, 16px gap, 12px horizontal padding):
  ┌──────────────────┬──────────────────┐
  │  [Flask icon]    │  [Person icon]   │
  │  Анализ          │  Консультация    │
  │  #CCFBF1 bg      │  #CFFAFE bg      │
  ├──────────────────┼──────────────────┤
  │  [Scan icon]     │  [File icon]     │
  │  Исследование    │  Другое          │
  │  #EDE9FE bg      │  #F3F4F6 bg      │
  └──────────────────┴──────────────────┘

Each type card: 80pt height, 12px radius, centered icon 36pt + label Body Med below.
Press state: scale 0.96, border Primary.

═══════════════════════════════════════════
SCREEN 7 — ADD CONSULTATION
═══════════════════════════════════════════

Navigation: "← Новое событие" / "Консультация" (H1) / "×" close.

Form (scroll):
  InputField: "Специальность врача"  placeholder "Терапевт, кардиолог..."
  InputField: "Имя врача"            placeholder "Необязательно"
  DatePicker row: "Дата приёма"      "4 мая 2026 ▼"  teal text
  InputField multiline: "Диагноз"    placeholder "Поставленный диагноз или подозрение"
  InputField multiline: "Назначения" placeholder "Препараты, процедуры, режим..."
  InputField multiline: "Рекомендации" placeholder "Направления, повторный приём..."

  Divider.
  Section: "Привязать к гипотезе"
    HypothesisSelector: list of theme's hypotheses, each row:
      [HypothesisName] + [ImpactSegment: Подтверждает | Нейтрально | Опровергает]
      ImpactSegment: 3-option segmented, active option colored (green/gray/red)

Sticky bottom:
  [Сохранить консультацию] — PrimaryButton.

═══════════════════════════════════════════
SCREEN 8 — ADD ANALYSIS (ручной ввод)
═══════════════════════════════════════════

Navigation: "← Новое событие" / "Анализ" (H1) / "×" close.

Form (scroll):
  InputField: "Название анализа *"  placeholder "Общий анализ крови, биохимия..."
  DatePicker row: "Дата сдачи"
  InputField: "Лаборатория"         placeholder "Необязательно"

  Section header: "Показатели" (H2) + count badge (teal)

  ParameterInputRow × N (repeatable):
    ┌────────────────────────────────────────────┐
    │ [Название параметра         ▼] [Ед. ▼] [×] │
    │  Значение [    ] / Норма [    ] – [    ]    │
    └────────────────────────────────────────────┘
    After value entry: inline status indicator appears.
    "Название параметра" is a searchable dropdown or freetext.
    "×" removes row.

  [+ Добавить показатель] — text button, teal, full width, dashed border top.

  Note: GUSIK_THINK 32pt inline + "Введите нормы с бланка анализа" (Caption Secondary)

  Divider.
  HypothesisSelector (same as consultation screen).

Sticky bottom:
  [Сохранить анализ] — PrimaryButton.

═══════════════════════════════════════════
SCREEN 9 — ADD RESEARCH (исследование)
═══════════════════════════════════════════

Navigation: "← Новое событие" / "Исследование" (H1) / "×" close.

Form:
  InputField: "Тип исследования"  placeholder "МРТ, КТ, УЗИ, рентген..."
  DatePicker row: "Дата исследования"
  InputField multiline 4 rows: "Заключение"  placeholder "Текст заключения врача-диагноста"

  Section: "Прикрепить фото документа"
    Photo zone (dashed teal border, 12px radius, 120pt height):
      GUSIK_DOCTOR 40pt centered
      "Нажмите, чтобы сфотографировать" (Body, Secondary)
      "или выбрать из галереи" (Caption, Secondary)
    After photo added: thumbnail preview card with "×" remove.

  HypothesisSelector.

Sticky bottom:
  [Сохранить исследование] — PrimaryButton.

═══════════════════════════════════════════
SCREEN 10 — EVENT DETAIL
═══════════════════════════════════════════

Navigation: back arrow + event type + date. "⋮" action menu: Edit / Delete.

For ANALYSIS detail:
  Header card: analysis name (H1) + date + lab badge.

  Section "Показатели":
    ParameterRow × N (full width, alternating #F0FDFA / white rows)
    Each row: name + [StatusDot value unit] + "норма min–max"

  AIInsightCard below table.

  Section "Файлы" (if any):
    Photo thumbnails in horizontal scroll, 80×80pt, 8px radius.

  Divider.

  Section "Резолюция":
    Row: "Это событие..." (Body Secondary)
    ResolutionButton pair.
    If set: locked state + comment field:
      "Ваш комментарий" multiline (optional).

  Section "Влияние на гипотезы":
    HypothesisSelector with current impact shown.

═══════════════════════════════════════════
SCREEN 11 — PROFILE
═══════════════════════════════════════════

Background: #F0FDFA.

Avatar area (centered, top):
  Circle 80pt: Primary bg + white goose silhouette icon (simplified Gusik).
  User name (H1) below.
  Email (Caption Secondary) below name.
  [Редактировать] — small outlined teal button.

Settings sections (list style):
  Section "Профиль":
    Row: 👤 Личные данные (имя, пол, дата рождения) →
    Row: 🔒 Безопасность →

  Section "Данные":
    Row: 📋 Согласие на обработку данных →

  Section "О приложении":
    Row: Версия 1.0.0 (no chevron)
    Row: 🦢 Про Гусика →

  Danger section:
    [Выйти из аккаунта] — full width, Danger color, outlined, 52pt.

═══════════════════════════════════════════
EMPTY STATES SPECIFICATIONS
═══════════════════════════════════════════

All empty states centered vertically in their container.
Structure: [Gusik variant 64pt] + [Title H2] + [Body text] + [CTA optional]

Dashboard no themes:
  GUSIK_WAVE. "Начни своё расследование"
  "Создай первую тематику — и Гусик поможет разобраться, почему тебе плохо."
  [Создать тематику] PrimaryButton

Timeline empty:
  GUSIK_SEARCH. "Пока пусто"
  "Добавь первое событие: консультацию, анализ или исследование."
  [Добавить событие] outlined teal

Hypotheses empty:
  GUSIK_THINK. "Гипотез пока нет"
  "Гипотеза — это версия причины проблемы. Добавь хотя бы одну."
  [Добавить гипотезу] outlined teal

Symptoms empty:
  GUSIK_WAVE. "Симптомы не добавлены"
  "Опиши, что ощущаешь — это поможет Гусику найти закономерности."

═══════════════════════════════════════════
INTERACTIONS & STATES
═══════════════════════════════════════════

Every interactive element needs:
  Default / Press (0.97 scale + shadow reduce) / Disabled (40% opacity) /
  Loading (skeleton shimmer, teal-50 to teal-100) / Error (Danger border + message)

Transitions:
  Screen push: 300ms ease-out, horizontal slide right (iOS native feel)
  Bottom sheet: 280ms spring, slides from bottom
  FAB: scale-in 200ms on screen mount
  Cards: fade-in 150ms stagger (50ms each) on list load
  Tab switch: content cross-fade 150ms

Skeleton loading:
  Background: gradient animate #CCFBF1 → #F0FDFA → #CCFBF1 (shimmer)
  ThemeCard skeleton: 3 lines placeholder
  EventCard skeleton: icon circle + 2 lines

Resolution button selection:
  Tap: scale 1.05 → 1.0 spring + haptic (medium impact)
  Fill animation: color fill left-to-right 200ms

═══════════════════════════════════════════
ACCESSIBILITY
═══════════════════════════════════════════

Minimum touch target: 44×44pt (Apple HIG)
Color contrast: all text pairs pass WCAG AA (4.5:1 for body, 3:1 for large)
Never use color as sole indicator — always pair with icon or label
Focus rings for keyboard navigation: 2pt Primary outline
VoiceOver labels: all icon buttons labeled in Russian
Gusik illustrations: alt text provided for screen readers
```
