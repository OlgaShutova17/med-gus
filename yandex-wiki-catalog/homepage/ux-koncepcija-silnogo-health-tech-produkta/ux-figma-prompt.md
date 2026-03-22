---
title: Figma AI — промпт для проектирования интерфейса
---

Готовый промпт для Figma AI-агента (Make Designs / FigJam AI / Anima). Вставить как есть.

---

## ПРОМПТ

```
Design a mobile-first health tracking app called "МедДневник" (MedDnevnik).
The app helps users investigate their health problems — not just store data,
but understand WHY they feel bad. The core model is:
Problem → Hypotheses → Events → Evidence → Outcome.

---

DESIGN SYSTEM

Style: Medical-grade minimalism. Clean, trustworthy, calm.
Platform: Mobile (iOS/Android primary), responsive web secondary.
Grid: 4-column mobile (16px margins), 12-column desktop.

Color palette:
- Background:    #F8F9FB (off-white, main)
- Surface:       #FFFFFF (cards, modals)
- Primary:       #2563EB (blue — actions, links, active states)
- Primary light: #EFF6FF (blue tint for selected items)
- Success:       #16A34A (green — normal/confirmed/helped)
- Warning:       #D97706 (amber — deviation, testing status)
- Danger:        #DC2626 (red — critical values, rejected)
- Text primary:  #111827
- Text secondary:#6B7280
- Border:        #E5E7EB
- Divider:       #F3F4F6

Typography:
- Font: Inter (or SF Pro on iOS)
- H1: 22px / 700 (screen titles)
- H2: 17px / 600 (card titles, section headers)
- Body: 15px / 400 (main content)
- Caption: 13px / 400 (metadata, dates, labels)
- Mono: 14px / 500 (medical values, numbers)

Status badge colors:
- new:       #F3F4F6 bg, #6B7280 text
- testing:   #FEF3C7 bg, #D97706 text
- confirmed: #DCFCE7 bg, #16A34A text
- rejected:  #FEE2E2 bg, #DC2626 text
- helped:    #DCFCE7 bg, #16A34A text
- not_helped:#FEE2E2 bg, #DC2626 text

Value status indicators (inline):
- Normal:   #16A34A dot + green text
- Deviation:#D97706 dot + amber text
- Critical: #DC2626 dot + red text + bold

---

SCREEN 1 — DASHBOARD (home screen)

Layout: Vertical scroll. Status bar + navigation bar at bottom.

Navigation bar (bottom, 5 tabs):
  Home (filled icon) | Problems | Add (+) | Analytics | Profile

Header section:
  - "Добро пожаловать, [Name]" (H2, secondary color)
  - Date, e.g. "23 марта 2026" (Caption)

Section: "Мои проблемы" (H2 + "Все →" link)
  Problem cards (horizontal scroll or 1-column list):
    Card structure:
      - Problem title (H2, bold)
      - Leading hypothesis chip: "[HypothesisName] · [XX]%" (Primary color, small badge)
      - Status badge (active/resolved/archived)
      - Last event date (Caption, secondary)
    Example cards:
      Card 1: "Хроническая усталость" | "Дефицит железа · 72%" | active | "15 мар"
      Card 2: "Мигрени"               | "Хронический стресс · 45%" | active | "10 мар"

Section: "Последние события" (H2)
  Event list items (compact):
    - Icon by type (flask=analysis, person=consultation, scan=research, other)
    - Event name + problem tag
    - Date (Caption, right-aligned)
  Examples:
    🧪 Общий анализ крови · Усталость       15 мар
    👤 Консультация терапевта · Усталость    10 мар

Section: "AI Инсайты" (H2 + robot icon)
  Insight cards (colored left border = Primary):
    - Icon (lightbulb)
    - Short insight text (Body)
    - "Подробнее →" link
  Examples:
    "Ферритин снижается последние 6 месяцев — возможный дефицит железа"
    "Мигрени чаще возникают после недосыпания"

---

SCREEN 2 — PROBLEM PAGE (main product screen)

Header:
  - Back arrow + "Проблемы" breadcrumb
  - Problem title large (H1): "Хроническая усталость"
  - Status badge: "Активная"

AI Summary card (prominent, blue-tinted surface):
  - Small "AI" badge (Primary color)
  - "Вероятная причина:" label (Caption)
  - Hypothesis name (H2, bold): "Дефицит железа"
  - Confidence bar: [███████░░░] 72%
  - "Обновлено 15 мар" (Caption)

Tab bar (below AI card, 4 tabs):
  [ Timeline ] [ Гипотезы ] [ Симптомы ] [ Аналитика ]
  Active tab: Primary underline, bold text.

FAB button (bottom-right): "+" (add event)

---

SCREEN 2A — TIMELINE TAB

Chronological feed, newest first.
Group by month if >10 events.

Event card:
  ┌─────────────────────────────────────┐
  │ [Icon]  Анализ крови          15 мар│
  │         Общий анализ                │
  │                                     │
  │  Ферритин   10 мкг/л  🔴 критично  │
  │  Гемоглобин 120 г/л   🟡 отклон.  │
  │                                     │
  │  Влияние на гипотезы:               │
  │  ✓ Дефицит железа   ✗ Гипотиреоз  │
  │                                     │
  │  [Помогло] [Не помогло]             │
  └─────────────────────────────────────┘

Event types — icons and accent colors:
  🧪 Анализ        — blue accent
  👤 Консультация  — teal accent
  🔬 Исследование  — purple accent
  📝 Другое        — gray accent

Resolution buttons:
  "Помогло"     — outlined green button
  "Не помогло"  — outlined red button
  When selected: filled button, locked state

---

SCREEN 2B — HYPOTHESES TAB

Section title: "Гипотезы причин" + "Добавить" button (text, Primary)

Hypothesis card (expanded):
  ┌─────────────────────────────────────┐
  │  Дефицит железа           [testing] │
  │  ████████░░  72%                    │
  │                                     │
  │  Подтверждения:                     │
  │  ✓ ферритин ↓   ✓ гемоглобин ↓    │
  │  ✓ усталость                        │
  │                                     │
  │  Опровержения:                      │
  │  — нет                              │
  │                                     │
  │  [Курсы лечения (1)]  [Подробнее →]│
  └─────────────────────────────────────┘

Evidence chips (inline tags):
  ✓ confirmed evidence: green chip (#DCFCE7 bg, #16A34A text, checkmark icon)
  ✗ rejected evidence:  red chip   (#FEE2E2 bg, #DC2626 text, cross icon)

Hypothesis statuses → badge styles (from design system above).

---

SCREEN 2C — ANALYTICS TAB

Parameter selector: horizontal scroll chips
  [ Ферритин ✓ ] [ Гемоглобин ] [ Глюкоза ] [ ТТГ ]

Period selector: segmented control
  [ Неделя ] [ Месяц ✓ ] [ Квартал ]

Chart area (line chart):
  - Y axis: value with unit
  - X axis: dates
  - Line: Primary blue (#2563EB), 2px stroke
  - Reference range band: light green fill (#F0FDF4)
  - Two dashed horizontal lines: min and max reference (Success color, dashed)
  - Data points: filled circles, color by status (green/amber/red)
  - Tooltip on tap: card with date, value, status, ref range

Below chart — AI Insight card:
  "Ферритин снижается последние 6 месяцев. Рекомендуется повторный анализ."

---

SCREEN 3 — ADD EVENT (bottom sheet or full screen modal)

Title: "Добавить событие"
Problem selector: "К проблеме: Хроническая усталость ▼" (chip, tappable)

Event type grid (2×2 cards):
  ┌──────────┬──────────┐
  │  🧪      │  👤      │
  │  Анализ  │ Консульт.│
  ├──────────┼──────────┤
  │  🔬      │  📝      │
  │ Исследов.│  Другое  │
  └──────────┴──────────┘

Each card: icon (48px), label, rounded corners, border, tap = navigate to form.

---

SCREEN 4 — ADD ANALYSIS (form)

Header: "Новый анализ" + close (×)

Toggle at top:
  [ 📎 Загрузить файл ] [ ✏️ Ввести вручную ]
  Active: Primary filled. Inactive: outlined.

FILE MODE:
  Upload zone (dashed border, rounded):
    Cloud upload icon (48px, Secondary color)
    "Перетащите файл или нажмите для выбора"
    "PDF, JPG, PNG · до 25 МБ" (Caption)
  After upload: file preview card with name + size + remove (×)

  After OCR: extracted parameters table:
    ┌──────────────┬──────────┬───────┬──────────────┐
    │ Параметр     │ Значение │ Ед.   │ Норма        │
    ├──────────────┼──────────┼───────┼──────────────┤
    │ Гемоглобин   │ 120      │ г/л   │ 120–160      │
    │ Ферритин   🔴│ 10       │ мкг/л │ 20–150       │
    └──────────────┴──────────┴───────┴──────────────┘
    Note: "Проверьте данные перед сохранением" (Caption, amber)
    Tapping a row opens inline edit.

MANUAL MODE:
  Analysis type: searchable dropdown "Общий анализ крови ▼"
  Date: date picker "15 марта 2026"
  Lab: text field (optional) "Название лаборатории"
  Parameters: repeatable row group
    [ Параметр ▼ ] [ Значение ] [ Ед. ▼ ] [ + ]
  Add parameter button: "+ Добавить показатель" (text, Primary)

Common bottom:
  Hypothesis selector: "Привязать к гипотезе: Дефицит железа ▼"
  Primary button: "Сохранить" (full-width, 52px height)

---

SCREEN 5 — ANALYSIS DETAIL

Header: "Общий анализ крови · 15 мар 2026"
Back arrow. Action menu (⋮): Edit, Delete, Share.

Parameters table (full width):
  Each row:
    Parameter name (Body)
    Value with status dot (Mono font, colored)
    Reference range (Caption, secondary)
    Status label: "норма" / "↓ ниже нормы" / "↑ выше нормы" / "↓↓ критично"

AI Interpretation card (blue tinted):
  Robot icon + "AI Интерпретация"
  Text: "Ферритин значительно ниже нормы (10 мкг/л при норме 20–150).
         Возможный дефицит железа. Рекомендуется консультация терапевта."
  Disclaimer (Caption, secondary): "Носит ознакомительный характер"

Attached files section (if any):
  File chips with preview icon, name, open button.

---

SCREEN 6 — AI ASSISTANT (chat)

Header: "AI Ассистент" + small disclaimer icon (ⓘ)

Chat messages:
  User messages: right-aligned, Primary blue bubble, white text
  AI messages: left-aligned, Surface (#FFFFFF) bubble, border, dark text

AI message with evidence:
  ┌─────────────────────────────────────┐
  │ 🤖  Основная возможная причина —    │
  │      дефицит железа.                │
  │                                     │
  │  Это подтверждают:                  │
  │  • ферритин 10 мкг/л (ниже нормы)  │
  │  • снижение гемоглобина             │
  │  • симптомы усталости               │
  │                                     │
  │  Рекомендую:                        │
  │  • сдать анализ на железо и B12     │
  │  • обратиться к терапевту           │
  │                                     │
  │  ⚠ Не является медицинским диагнозом│
  └─────────────────────────────────────┘

Input area (pinned bottom):
  TextField: "Задайте вопрос о своём здоровье..."
  Send button (Primary, arrow icon)
  Suggested questions (scrollable chips above input):
    "Почему мне плохо?"  "Что проверить?"  "К какому врачу?"

---

COMPONENT LIBRARY (to design)

1. ProblemCard — title, hypothesis chip, status badge, last event date
2. EventCard — type icon, title, date, value rows, hypothesis impact chips, resolution buttons
3. HypothesisCard — title, status badge, confidence bar, evidence chips, actions
4. ParameterRow — name, value (mono), status dot, reference range
5. AIInsightCard — robot icon, text, disclaimer
6. StatusBadge — 5 variants: new/testing/confirmed/rejected + active/resolved
7. ValueChip — 3 variants: normal/deviation/critical
8. EvidenceChip — 2 variants: supports (green ✓) / rejects (red ✗)
9. ConfidenceBar — label + percentage + filled progress bar (color by confidence level)
10. UploadZone — dashed border, icon, label, drag-active state
11. SegmentedControl — period/mode selector
12. FAB — floating action button (+)
13. BottomSheet — modal for add event
14. EmptyState — illustration + text + CTA (for screens with no data)

---

INTERACTIONS & STATES

Every interactive element needs:
  - Default state
  - Hover/Press state (10% darker)
  - Disabled state (50% opacity)
  - Loading state (skeleton or spinner)
  - Empty state (placeholder illustration + CTA)
  - Error state (red border + error message below)

Charts:
  - Empty: "Нет данных за выбранный период" + illustration
  - Single point: dot with label, no line
  - Normal: line chart with reference band

Resolution buttons:
  - Unset: both outlined
  - Helped selected: green filled, not-helped outlined
  - Not helped selected: red filled, helped outlined

---

ACCESSIBILITY

- Minimum touch target: 44×44pt
- Color is never the only indicator (always pair with icon or label)
- Focus rings for keyboard navigation (web)
- All icons have aria-label equivalents
```
